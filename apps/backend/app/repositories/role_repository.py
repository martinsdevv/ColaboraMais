from app.db.database import get_connection
from app.domain.role import Role


def create_role(role: Role):

    conn = get_connection()

    cursor = conn.execute(
        """
        INSERT INTO roles (name, department_id)
        VALUES (?, ?)
        """,
        (role.name, role.department_id),
    )

    conn.commit()

    return cursor.lastrowid


def list_roles():

    conn = get_connection()

    rows = conn.execute(
        """
        SELECT id, name, department_id
        FROM roles
        """
    ).fetchall()

    return [
        Role(
            id=row["id"],
            name=row["name"],
            department_id=row["department_id"],
        )
        for row in rows
    ]