from pydantic import BaseModel


class UserCreate(BaseModel):

    name: str
    email: str
    password: str
    role_id: int


class UserResponse(BaseModel):

    id: int
    name: str
    email: str
    role_id: int