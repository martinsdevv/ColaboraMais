from pydantic import BaseModel


class RoleCreate(BaseModel):

    name: str
    department_id: int


class RoleResponse(BaseModel):

    id: int
    name: str
    department_id: int