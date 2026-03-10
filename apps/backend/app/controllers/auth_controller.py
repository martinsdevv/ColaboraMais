from fastapi import APIRouter, HTTPException

from app.schemas.auth_schema import LoginRequest
from app.services import auth_service

router = APIRouter()


@router.post("/auth/login")
def login(data: LoginRequest):

    token = auth_service.login(data.email, data.password)

    if not token:
        raise HTTPException(status_code=401, detail="invalid credentials")

    return {"access_token": token}