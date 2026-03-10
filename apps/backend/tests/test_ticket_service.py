from app.services.ticket_service import create_ticket, list_tickets


class DummyTicket:
    title = "Ticket Service"
    description = "Teste service"
    author_id = 1
    department_target_id = 1


def test_service_create_ticket():
    ticket = DummyTicket()

    ticket_id = create_ticket(ticket)

    assert ticket_id > 0


def test_service_list_tickets():
    tickets = list_tickets()

    assert isinstance(tickets, list)