from pydantic import BaseModel


class TicketCreate(BaseModel):
    title: str
    description: str
    department_target_id: int