from fastapi import APIRouter
from app.schemas.ticket_schema import TicketCreate
from app.schemas.ticket_status_schema import TicketStatusUpdate
from app.services import ticket_service
from fastapi import Depends
from app.security.dependencies import get_current_user

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)


@router.post("/tickets")
def create_ticket(
    ticket: TicketCreate,
    user=Depends(get_current_user)
):

    ticket_id = ticket_service.create_ticket(
        ticket,
        author_id=user["id"]
    )

    return {"ticket_id": ticket_id}


@router.get("/tickets")
def list_tickets(
    status: str | None = None,
    department: int | None = None,
    author: int | None = None
):

    return ticket_service.list_tickets(status, department, author)

@router.patch("/tickets/{ticket_id}/status")
def update_status(
    ticket_id: int,
    data: TicketStatusUpdate
):

    ticket_service.update_ticket_status(
        ticket_id,
        data.status,
        user["id"]
    )

    return {"status": "updated"}