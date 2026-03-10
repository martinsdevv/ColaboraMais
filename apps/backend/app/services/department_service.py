from app.repositories import department_repository
from app.domain.department import Department


def create_department(department_data):

    department = Department(
        name=department_data.name
    )

    return department_repository.create_department(department)


def list_departments():
    return department_repository.list_departments()