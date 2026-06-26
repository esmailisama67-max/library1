from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.users.schemas import UserCreate
from app.users.service import UserService

router = APIRouter()

@router.post("/register")
def register(
        user: UserCreate,
        db: Session = Depends(get_db)
):

    service = UserService(db)

    return service.register(user)