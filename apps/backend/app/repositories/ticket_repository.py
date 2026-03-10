from app.db.database import get_connection
from app.domain.ticket import Ticket


def create_ticket(ticket):
    conn = get_connection()

    cursor = conn.execute(
        """
        INSERT INTO tickets (title, description, author_id, department_target_id)
        VALUES (?, ?, ?, ?)
        """,
        (
            ticket.title,
            ticket.description,
            ticket.author_id,
            ticket.department_target_id,
        ),
    )

    conn.commit()

    ticket_id = cursor.lastrowid

    conn.close()

    return ticket_id


def list_tickets():
    conn = get_connection()

    rows = conn.execute(
        "SELECT id, title, description, status FROM tickets"
    ).fetchall()

    return [
        Ticket(
            id=row["id"],
            title=row["title"],
            description=row["description"],
            author_id=None,
            department_target_id=None,
            status=row["status"],
        )
        for row in rows
    ]