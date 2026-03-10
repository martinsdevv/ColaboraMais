from fastapi import APIRouter, Depends

from app.schemas.user_schema import UserCreate, UserResponse
from app.services import user_service
from app.security.dependencies import get_current_user

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)


@router.post("/users")
def create_user(user: UserCreate):

    user_id = user_service.create_user(user)

    return {"user_id": user_id}


@router.get("/users", response_model=list[UserResponse])
def list_users():

    return user_service.list_users()