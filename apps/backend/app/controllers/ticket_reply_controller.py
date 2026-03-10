from fastapi import APIRouter, Depends

from app.schemas.ticket_reply_schema import TicketReplyCreate
from app.services import ticket_reply_service
from app.security.dependencies import get_current_user

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)


@router.post("/tickets/{ticket_id}/replies")
def create_reply(
    ticket_id: int,
    data: TicketReplyCreate,
    user=Depends(get_current_user)
):

    reply_id = ticket_reply_service.create_reply(
        ticket_id,
        data.message,
        data.type,
        user["id"]
    )

    return {"reply_id": reply_id}


@router.get("/tickets/{ticket_id}/replies")
def list_replies(
    ticket_id: int
):

    return ticket_reply_service.list_replies(ticket_id)