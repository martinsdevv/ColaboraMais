from fastapi import APIRouter
from app.schemas.ticket_schema import TicketCreate
from app.services import ticket_service

router = APIRouter()


@router.post("/tickets")
def create_ticket(ticket: TicketCreate):
    ticket_id = ticket_service.create_ticket(ticket)

    return {"ticket_id": ticket_id}


@router.get("/tickets")
def list_tickets():
    return ticket_service.list_tickets()