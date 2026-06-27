from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.users.repository import UserRepository
from app.database.session import get_db
from app.users.schemas import UserCreate
from app.users.service import UserService
from typing import List
from app.auth.dependencies import get_current_user
from app.database.models import User
from app.users.schemas import UserResponse



router = APIRouter()

@router.post("/register")
def register(
        user: UserCreate,
        db: Session = Depends(get_db)
):

    service = UserService(db)

    return service.register(user)

@router.get("/users", response_model=List[UserResponse])

@router.get("/users")
def get_all_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # فقط ادمین اجازه دارد
    if current_user.role != "admin":
        return {"detail": "Access denied"}

    repo = UserRepository(db)
    users = repo.get_all()

    return users


