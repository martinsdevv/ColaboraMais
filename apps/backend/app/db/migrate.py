import os
from pathlib import Path
from .database import get_connection

BASE_DIR = Path("/app")
SQL_DIR = BASE_DIR / "infra" / "sql"


def ensure_migrations_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS migrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            executed_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()


def get_executed_migrations(conn):
    rows = conn.execute("SELECT name FROM migrations").fetchall()
    return {row["name"] for row in rows}


def run_migrations():
    conn = get_connection()

    ensure_migrations_table(conn)

    executed = get_executed_migrations(conn)

    files = sorted(os.listdir(SQL_DIR))

    for file in files:

        if file in executed:
            continue

        path = SQL_DIR / file

        print(f"Running migration: {file}")

        with open(path) as f:
            sql = f.read()

        conn.executescript(sql)

        conn.execute(
            "INSERT INTO migrations (name) VALUES (?)",
            (file,)
        )

        conn.commit()

    conn.close()