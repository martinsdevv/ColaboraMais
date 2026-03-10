from app.repositories import ticket_reply_repository
from app.domain.ticket_reply import TicketReply
from app.services import audit_service


def create_reply(ticket_id, message, type, author_id):

    reply = TicketReply(
        ticket_id=ticket_id,
        author_id=author_id,
        message=message,
        type=type
    )

    audit_service.log_action(
        author_id,
        "ADD_REPLY",
        "ticket",
        ticket_id
    )

    return ticket_reply_repository.create_reply(reply)


def list_replies(ticket_id):

    return ticket_reply_repository.list_replies(ticket_id)