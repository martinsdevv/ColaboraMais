from fastapi import FastAPI
from app.db.migrate import run_migrations

app = FastAPI()


@app.on_event("startup")
def startup():
    run_migrations()


@app.get("/")
def health():
    return {"status": "ok"}