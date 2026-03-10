import sqlite3
import os
import time

def get_connection():
    # No Docker, use sempre o caminho absoluto que definimos no ENV
    db_path = os.getenv("DB_PATH", "/data/colaboramais.db")

    # Tenta criar a pasta, mas com tratamento de erro
    try:
        dir_name = os.path.dirname(db_path)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)
    except Exception as e:
        print(f">>> Erro ao criar pasta do banco: {e}")

    # O segredo: timeout de 5 segundos. 
    # Se o Windows travar o arquivo, o Python desiste e cospe um erro no log
    conn = sqlite3.connect(db_path, timeout=5)
    conn.row_factory = sqlite3.Row

    return conn