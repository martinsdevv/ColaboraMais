from app.db.database import get_connection
from app.domain.department import Department


def create_department(department: Department):

    conn = get_connection()

    cursor = conn.execute(
        """
        INSERT INTO departments (name)
        VALUES (?)
        """,
        (department.name,),
    )

    conn.commit()

    return cursor.lastrowid


def list_departments():

    conn = get_connection()

    rows = conn.execute(
        "SELECT id, name FROM departments"
    ).fetchall()

    return [
        Department(
            id=row["id"],
            name=row["name"],
        )
        for row in rows
    ]