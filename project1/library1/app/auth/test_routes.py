from fastapi import APIRouter, Depends
from app.auth.dependencies import get_current_user
from app.database.models import User

router = APIRouter()


# 👤 User Test Route
@router.get("/user/test")
def user_test(current_user: User = Depends(get_current_user)):
    return {
        "message": "User route working",
        "user": current_user.username
    }


# 👑 Admin Test Route
@router.get("/admin/test")
def admin_test(current_user: User = Depends(get_current_user)):
    return {
        "message": "Admin route working",
        "admin": current_user.username
    }