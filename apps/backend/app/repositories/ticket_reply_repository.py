from app.db.database import get_connection
from app.domain.ticket_reply import TicketReply


def create_reply(reply: TicketReply):

    conn = get_connection()

    cursor = conn.execute(
        """
        INSERT INTO ticket_replies
        (ticket_id, author_id, message, type)
        VALUES (?, ?, ?, ?)
        """,
        (
            reply.ticket_id,
            reply.author_id,
            reply.message,
            reply.type
        )
    )

    conn.commit()

    return cursor.lastrowid


def list_replies(ticket_id: int):

    conn = get_connection()

    rows = conn.execute(
        """
        SELECT id, ticket_id, author_id, message, type
        FROM ticket_replies
        WHERE ticket_id = ?
        ORDER BY id
        """,
        (ticket_id,)
    ).fetchall()

    return rows