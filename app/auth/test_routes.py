from fastapi import APIRouter, Depends
from app.auth.dependencies import get_current_user
from app.database.models import User

router = APIRouter(tags=["JWT Test"])


@router.get("/user/test")
def user_test(current_user: User = Depends(get_current_user)):
    return {
        "message": "JWT is valid",
        "username": current_user.username,
        "role": current_user.role,
        "email": current_user.email
    }


@router.get("/admin/test")
def admin_test(current_user: User = Depends(get_current_user)):

    if current_user.role != "admin":
        return {
            "message": "Access Denied"
        }

    return {
        "message": "Welcome Admin",
        "username": current_user.username,
        "role": current_user.role
    }