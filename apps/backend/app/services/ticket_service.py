from app.repositories import ticket_repository


def create_ticket(ticket):
    return ticket_repository.create_ticket(ticket)


def list_tickets():
    return ticket_repository.list_tickets()