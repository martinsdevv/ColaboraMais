from fastapi import FastAPI
from app.db.migrate import run_migrations
from app.controllers.ticket_controller import router as ticket_router
from app.controllers.department_controller import router as department_router
from app.controllers.user_controller import router as user_router
from app.controllers.role_controller import router as role_router
from app.controllers.auth_controller import router as auth_router
from app.controllers.me_controller import router as me_router
from app.controllers.ticket_reply_controller import router as reply_router

app = FastAPI()

app.include_router(ticket_router)
app.include_router(department_router)
app.include_router(user_router)
app.include_router(role_router)
app.include_router(auth_router)
app.include_router(me_router)
app.include_router(reply_router)

@app.on_event("startup")
def startup():
    run_migrations()


@app.get("/")
def health():
    return {"status": "ok"}
