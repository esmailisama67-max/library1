from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.users.repository import UserRepository
from app.database.session import get_db
from app.users.schemas import UserCreate
from app.users.service import UserService , get_user_service
from typing import List
from app.auth.dependencies import get_current_user , admin_required
from app.database.models import User
from app.users.schemas import UserResponse, UserUpdate, PasswordChange
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/users")
def get_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    repo = UserRepository(db)
    users = repo.get_all()

    return {
        "count": len(users),
        "users": users
    }
    
@router.get(
    "",
    response_model=List[UserResponse]
)
def get_users(
    skip: int = Query(
        default=0,
        ge=0,
        description="تعداد رکوردهایی که رد می‌شوند"
    ),

    limit: int = Query(
        default=10,
        ge=1,
        le=100,
        description="حداکثر تعداد کاربران"
    ),

    service: UserService = Depends(get_user_service),

    current_user: User = Depends(admin_required)

):

    return service.get_users(
        skip,
        limit
    )
    
@router.get( "",response_model=List[UserResponse] )
def get_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    service = UserService(db)
    return service.get_users(skip, limit)

@router.get(
    "/{user_id}",
    response_model=List[UserResponse]
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    service = UserService(db)
    return service.get_user(user_id)

@router.put(
    "/{user_id}",
    response_model=List[UserResponse]
)
def update_user(
    user_id: int,
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    service = UserService(db)
    return service.update_user(user_id, data)

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    service = UserService(db)
    service.delete_user(user_id)
    
@router.patch(
    "/{user_id}/activate",
    response_model=List[UserResponse]
)
def activate_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    service = UserService(db)
    return service.activate_user(user_id)

@router.patch(
    "/{user_id}/deactivate",
    response_model=List[UserResponse]
)
def deactivate_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    service = UserService(db)
    return service.deactivate_user(user_id)

@router.get(
    "/profile",
    response_model=List[UserResponse]
)
def get_profile(
    current_user: User = Depends(get_current_user)
):
    return current_user

@router.put(
    "/profile",
    response_model=List[UserResponse]
)
def update_profile(
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service = UserService(db)
    return service.update_profile(current_user, data)

@router.put(
    "/change-password"
)
def change_password(
    data: PasswordChange,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service = UserService(db)
    return service.change_password(current_user, data)