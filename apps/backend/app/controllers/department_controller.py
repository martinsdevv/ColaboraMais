from fastapi import APIRouter, Depends
from app.schemas.department_schema import DepartmentCreate
from app.services import department_service
from app.security.dependencies import get_current_user

router = APIRouter()


@router.post("/departments")
def create_department(
    department: DepartmentCreate,
    user=Depends(get_current_user)
):

    department_id = department_service.create_department(department)

    return {"department_id": department_id}


@router.get("/departments")
def list_departments(
    user=Depends(get_current_user)
):

    return department_service.list_departments()