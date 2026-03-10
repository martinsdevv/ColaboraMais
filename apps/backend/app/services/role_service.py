from app.repositories import role_repository
from app.domain.role import Role


def create_role(role_data):

    role = Role(
        name=role_data.name,
        department_id=role_data.department_id,
    )

    return role_repository.create_role(role)


def list_roles():

    return role_repository.list_roles()