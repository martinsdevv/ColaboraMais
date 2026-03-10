from fastapi import APIRouter, Depends
from app.security.dependencies import get_current_user
from app.services.ticket_service import count_open_tickets

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)

@router.get("/metrics")
def metrics():

    return {
        "open_tickets": count_open_tickets()
    }