from fastapi import APIRouter

from app.schemas.role_schema import RoleCreate
from app.services import role_service
from fastapi import Depends
from app.security.dependencies import get_current_user

router = APIRouter()


@router.post("/roles")
def create_role(role: RoleCreate):

    role_id = role_service.create_role(role)

    return {"role_id": role_id}


@router.get("/roles")
def list_roles():

    return role_service.list_roles()