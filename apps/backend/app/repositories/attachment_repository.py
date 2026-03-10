from app.db.database import get_connection
from app.domain.attachment import Attachment


def create_attachment(att):

    conn = get_connection()

    cursor = conn.execute(
        """
        INSERT INTO attachments
        (ticket_id, file_path, file_type)
        VALUES (?, ?, ?)
        """,
        (
            att.ticket_id,
            att.file_path,
            att.file_type
        )
    )

    conn.commit()

    return cursor.lastrowid


def list_attachments(ticket_id):

    conn = get_connection()

    rows = conn.execute(
        """
        SELECT id, ticket_id, file_path, file_type
        FROM attachments
        WHERE ticket_id = ?
        """,
        (ticket_id,)
    ).fetchall()

    return rows