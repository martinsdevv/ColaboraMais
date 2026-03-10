from pydantic import BaseModel


class TicketCreate(BaseModel):
    title: str
    description: str
    author_id: int
    department_target_id: int