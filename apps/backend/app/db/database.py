import sqlite3
import os


def get_connection():
    db_path = os.getenv("DB_PATH", "data/colaboramais.db")

    # cria pasta se não existir
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    return conn