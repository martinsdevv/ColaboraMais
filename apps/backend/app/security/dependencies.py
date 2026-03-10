from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.security.auth import decode_token
from app.repositories import user_repository

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    try:
        payload = decode_token(token)
    except Exception:
        raise HTTPException(status_code=401, detail="invalid token")

    user_id = payload.get("user_id")

    user = user_repository.get_user_by_id(user_id)

    if not user:
        raise HTTPException(status_code=401, detail="user not found")

    return user