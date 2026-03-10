from app.repositories import attachment_repository
from app.domain.attachment import Attachment


def create_attachment(ticket_id, file_path, file_type):

    att = Attachment(
        ticket_id,
        file_path,
        file_type
    )

    return attachment_repository.create_attachment(att)


def list_attachments(ticket_id):

    return attachment_repository.list_attachments(ticket_id)