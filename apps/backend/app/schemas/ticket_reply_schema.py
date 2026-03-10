from pydantic import BaseModel


class TicketReplyCreate(BaseModel):

    message: str
    type: str


class TicketReplyResponse(BaseModel):

    id: int
    ticket_id: int
    author_id: int
    message: str
    type: str