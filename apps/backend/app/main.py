from fastapi import FastAPI
from app.db.migrate import run_migrations
from app.controllers.ticket_controller import router as ticket_router
from app.controllers.department_controller import router as department_router

app = FastAPI()

app.include_router(ticket_router)
app.include_router(department_router)

@app.on_event("startup")
def startup():
    run_migrations()


@app.get("/")
def health():
    return {"status": "ok"}
