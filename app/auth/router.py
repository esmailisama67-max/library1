from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.database.session import get_db

from app.users.schemas import UserCreate, UserLogin
from app.users.service import UserService
from app.auth.service import AuthService
from app.auth.dependencies import get_current_user
from app.database.models import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(
        data: UserCreate,
        db: Session = Depends(get_db)
):

    service = UserService(db)

    user = service.register(data)

    return {
        "message": "User created successfully",
        "user_id": user.id
    }
    
@router.post("/login")
def login(
        data: UserLogin,
        db: Session = Depends(get_db)
):

    service = UserService(db)

    return service.login(data) 

@router.post("/refresh")
def refresh():

    return {
        "message": "Coming soon"
    }

@router.post("/logout")
def logout():

    return {
        "message": "Logged out successfully"
    }

@router.get("/me")
def get_me(
        current_user: User = Depends(
            get_current_user
        )
):

    return current_user
