from fastapi import Depends
from app.database.session import get_db
from sqlalchemy.orm import Session

from app.users.repository import UserRepository
from app.users.service import UserService

from app.logs.repository import LogRepository
from app.logs.service import LogService


def get_user_service(db: Session = Depends(get_db)):
    repo = UserRepository(db)
    return UserService(repo)


def get_log_service(db: Session = Depends(get_db)):
    repo = LogRepository(db)
    return LogService(repo)