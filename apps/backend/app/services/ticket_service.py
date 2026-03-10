from app.repositories import ticket_repository
from app.services import ticket_reply_service


def create_ticket(ticket):
    return ticket_repository.create_ticket(ticket)


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