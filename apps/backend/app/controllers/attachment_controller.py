from fastapi import APIRouter, Depends

from app.services import attachment_service
from app.security.dependencies import get_current_user

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)


@router.post("/tickets/{ticket_id}/attachments")
def add_attachment(ticket_id: int):

    file_path = "uploads/test.pdf"

    attachment_id = attachment_service.create_attachment(
        ticket_id,
        file_path,
        "file"
    )

    return {"attachment_id": attachment_id}


@router.get("/tickets/{ticket_id}/attachments")
def list_attachments(ticket_id: int):

    return attachment_service.list_attachments(ticket_id)