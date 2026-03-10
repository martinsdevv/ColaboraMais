from fastapi import APIRouter
from app.schemas.department_schema import DepartmentCreate
from app.services import department_service

router = APIRouter()


@router.post("/departments")
def create_department(department: DepartmentCreate):

    department_id = department_service.create_department(department)

    return {"department_id": department_id}


@router.get("/departments")
def list_departments():

    return department_service.list_departments()