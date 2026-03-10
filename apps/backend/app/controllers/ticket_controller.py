from fastapi import APIRouter
from app.schemas.ticket_schema import TicketCreate
from app.schemas.ticket_status_schema import TicketStatusUpdate
from app.services import ticket_service
from fastapi import Depends
from app.security.dependencies import get_current_user

router = APIRouter()


@router.post("/tickets")
def create_ticket(ticket: TicketCreate, user=Depends(get_current_user)):
    ticket_id = ticket_service.create_ticket(ticket)

    return {"ticket_id": ticket_id}


@router.get("/tickets")
def list_tickets(user=Depends(get_current_user)):
    return ticket_service.list_tickets()

@router.patch("/tickets/{ticket_id}/status")
def update_status(
    ticket_id: int,
    data: TicketStatusUpdate,
    user=Depends(get_current_user)
):

    ticket_service.update_ticket_status(
        ticket_id,
        data.status,
        user["id"]
    )

    return {"status": "updated"}