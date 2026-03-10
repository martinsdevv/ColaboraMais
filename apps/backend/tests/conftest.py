import sys
import os
import tempfile
from pathlib import Path

# adicionar backend ao path
sys.path.append(str(Path(__file__).resolve().parents[1]))

# criar banco temporário
db_fd, db_path = tempfile.mkstemp()

os.environ["DB_PATH"] = db_path

from app.db.migrate import run_migrations


def pytest_sessionstart(session):
    run_migrations()


def pytest_sessionfinish(session, exitstatus):
    os.close(db_fd)