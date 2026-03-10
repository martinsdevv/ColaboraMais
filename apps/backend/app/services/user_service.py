import hashlib

from app.repositories import user_repository
from app.domain.user import User


def hash_password(password: str):

    return hashlib.sha256(password.encode()).hexdigest()


def create_user(user_data):

    password_hash = hash_password(user_data.password)

    user = User(
        name=user_data.name,
        email=user_data.email,
        password_hash=password_hash,
        role_id=user_data.role_id,
    )

    return user_repository.create_user(user)


def list_users():

    return user_repository.list_users()