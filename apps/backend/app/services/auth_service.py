import hashlib

from app.repositories import user_repository
from app.security.auth import create_access_token
from app.services import audit_service


def hash_password(password: str):

    return hashlib.sha256(password.encode()).hexdigest()


def login(email: str, password: str):

    user = user_repository.get_user_by_email(email)

    if not user:
        return None

    password_hash = hash_password(password)

    if password_hash != user["password_hash"]:
        return None

    token = create_access_token(user["id"])

    audit_service.log_action(
        user["id"],
        "LOGIN",
        "user",
        user["id"]
    )

    return token