from app.repositories import ticket_repository
from app.services import ticket_reply_service
from app.services import audit_service


def create_ticket(ticket, user_id):

    ticket_id = ticket_repository.create_ticket(ticket)

    audit_service.log_action(
        user_id,
        "CREATE_TICKET",
        "ticket",
        ticket_id
    )

    return ticket_id


def list_tickets():
    return ticket_repository.list_tickets()


def update_ticket_status(ticket_id, status, user_id):

    ticket_repository.update_ticket_status(ticket_id, status)

    ticket_reply_service.create_reply(
        ticket_id,
        f"Status alterado para {status}",
        "ATUALIZACAO_STATUS",
        user_id
    )

    audit_service.log_action(
        user_id,
        "UPDATE_STATUS",
        "ticket",
        ticket_id,
        {"status": status}
    )


def count_open_tickets():

    return ticket_repository.count_open_tickets()