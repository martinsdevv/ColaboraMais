from app.repositories.ticket_repository import create_ticket, list_tickets


class DummyTicket:
    title = "Teste"
    description = "Descrição teste"
    author_id = 1
    department_target_id = 1


def test_create_ticket():
    ticket = DummyTicket()

    ticket_id = create_ticket(ticket)

    assert ticket_id is not None
    assert isinstance(ticket_id, int)


def test_list_tickets():
    ticket = DummyTicket()
    create_ticket(ticket)

    tickets = list_tickets()

    assert len(tickets) >= 1