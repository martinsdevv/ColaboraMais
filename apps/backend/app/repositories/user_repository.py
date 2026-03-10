from app.db.database import get_connection
from app.domain.user import User


def create_user(user: User):

    conn = get_connection()

    cursor = conn.execute(
        """
        INSERT INTO users (name, email, password_hash, role_id, active)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            user.name,
            user.email,
            user.password_hash,
            user.role_id,
            user.active,
        ),
    )

    conn.commit()

    return cursor.lastrowid


def list_users():

    conn = get_connection()

    rows = conn.execute(
        """
        SELECT id, name, email, role_id
        FROM users
        """
    ).fetchall()

    return [
        User(
            id=row["id"],
            name=row["name"],
            email=row["email"],
            password_hash=None,
            role_id=row["role_id"],
        )
        for row in rows
    ]

def get_user_by_email(email: str):

    conn = get_connection()

    row = conn.execute(
        """
        SELECT id, name, email, password_hash, role_id
        FROM users
        WHERE email = ?
        """,
        (email,),
    ).fetchone()

    if not row:
        return None

    return row

def get_user_by_id(user_id: int):

    conn = get_connection()

    row = conn.execute(
        """
        SELECT id, name, email, role_id, active
        FROM users
        WHERE id = ?
        """,
        (user_id,),
    ).fetchone()

    return row