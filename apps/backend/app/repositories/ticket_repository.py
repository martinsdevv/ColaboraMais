from app.db.database import get_connection


def create_ticket(data):

    conn = get_connection()

    cursor = conn.execute(
        """
        INSERT INTO tickets (title, description, author_id, department_target_id)
        VALUES (?, ?, ?, ?)
        """,
        (
            data["title"],
            data["description"],
            data["author_id"],
            data["department_target_id"],
        ),
    )

    conn.commit()

    ticket_id = cursor.lastrowid

    conn.close()

    return ticket_id


def list_tickets(status=None, department=None, author=None):

    conn = get_connection()

    query = "SELECT * FROM tickets WHERE 1=1"
    params = []

    if status:
        query += " AND status = ?"
        params.append(status)

    if department:
        query += " AND department_target_id = ?"
        params.append(department)

    if author:
        query += " AND author_id = ?"
        params.append(author)

    query += " ORDER BY created_at DESC"

    rows = conn.execute(query, params).fetchall()

    conn.close()

    return rows


def update_ticket_status(ticket_id: int, status: str):

    conn = get_connection()

    conn.execute(
        """
        UPDATE tickets
        SET status = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (status, ticket_id)
    )

    conn.commit()

    conn.close()


def count_open_tickets():

    conn = get_connection()

    row = conn.execute(
        """
        SELECT COUNT(*) as total
        FROM tickets
        WHERE status != 'CONCLUIDO'
        """
    ).fetchone()

    conn.close()

    return row["total"]