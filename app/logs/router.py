from typing import List

from fastapi import APIRouter, Depends

from app.auth.dependencies import admin_required

from app.logs.repository import LogRepository
from app.logs.schemas import LogResponse
from app.logs.service import LogService

from app.database.session import get_db


router = APIRouter(
    prefix="/logs",
    tags=["Logs"])

def get_log_service(db=Depends(get_db)):

    repo = LogRepository(db)

    return LogService(repo)

@router.get( "", response_model=List[LogResponse]
)
def get_logs(

    admin=Depends(admin_required),

    service: LogService = Depends(get_log_service)

):

    return service.get_all()

@router.get(
    "/{user_id}",
    response_model=List[LogResponse]
)
def get_user_logs(

    user_id: int,

    admin=Depends(admin_required),

    service: LogService = Depends(get_log_service)

):

    return service.get_user_logs(user_id)