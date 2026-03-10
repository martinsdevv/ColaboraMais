import os
import sqlite3
from pathlib import Path
from .database import get_connection

# Define a raiz do projeto de forma segura
# migrate.py está em app/db/, então subimos 2 níveis para chegar na raiz do código
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# No Docker, a estrutura é /app/infra/sql
# Localmente, usamos o BASE_DIR para achar a pasta infra
SQL_DIR = Path("/app/infra/sql")
if not SQL_DIR.exists():
    SQL_DIR = BASE_DIR / "infra" / "sql"

def ensure_migrations_table(conn):
    """Cria a tabela de controle de migrações se não existir."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS migrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            executed_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()

def get_executed_migrations(conn):
    """Retorna um set com os nomes das migrações já executadas."""
    cursor = conn.execute("SELECT name FROM migrations")
    return {row["name"] for row in cursor.fetchall()}

def run_migrations():
    """Lê os arquivos SQL e executa os que ainda não foram rodados."""
    print(f">>> Verificando migrações em: {SQL_DIR}")
    
    if not SQL_DIR.exists():
        print(f"!!! ERRO: Pasta de migrações não encontrada: {SQL_DIR}")
        return

    conn = get_connection()
    try:
        ensure_migrations_table(conn)
        executed = get_executed_migrations(conn)

        # Lista arquivos .sql em ordem alfabética (001, 002...)
        files = sorted([f for f in os.listdir(SQL_DIR) if f.endswith('.sql')])

        for file in files:
            if file in executed:
                continue

            print(f"--- Executando migração: {file}")
            path = SQL_DIR / file
            
            with open(path, "r", encoding="utf-8") as f:
                sql = f.read()

            # Executa o script e registra na tabela de controle
            conn.executescript(sql)
            conn.execute("INSERT INTO migrations (name) VALUES (?)", (file,))
            conn.commit()
            print(f"--- {file} aplicada com sucesso!")

    except Exception as e:
        print(f"!!! FALHA NA MIGRAÇÃO: {e}")
        conn.rollback()
        raise e
    finally:
        conn.close()