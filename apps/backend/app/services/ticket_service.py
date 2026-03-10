from app.repositories import ticket_repository
from app.services import ticket_reply_service
from app.services import audit_service


def create_ticket(ticket, author_id):

    ticket_data = {
        "title": ticket.title,
        "description": ticket.description,
        "author_id": author_id,
        "department_target_id": ticket.department_target_id
    }

    ticket_id = ticket_repository.create_ticket(ticket_data)

    audit_service.log_action(
        author_id,
        "CREATE_TICKET",
        "ticket",
        ticket_id
    )

    return ticket_id


def list_tickets(status=None, department=None, author=None):

    return ticket_repository.list_tickets(
        status=status,
        department=department,
        author=author
    )


def update_ticket_status(ticket_id, status, user_id):

    old_status = ticket_repository.get_ticket_status(ticket_id)

    ticket_repository.update_ticket_status(ticket_id, status)

    ticket_reply_service.create_reply(
        ticket_id,
        f"Status alterado de {old_status} para {status}",
        "ATUALIZACAO_STATUS",
        user_id
    )

    audit_service.log_action(
        user_id,
        "UPDATE_STATUS",
        "ticket",
        ticket_id,
        {
            "from": old_status,
            "to": status
        }
    )


def count_open_tickets():

    return ticket_repository.count_open_tickets()