from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.database.session import SessionLocal 
from app.database.models import User

from app.database.session import get_db
from app.database.models import User
from app.auth.jwt_handler import verify_token
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security import OAuth2
from fastapi import Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()


# ---------------- Current User ----------------

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials  # 👈 خطای مربوط به authorization , token  تایید

    payload = verify_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user_id = payload.get("sub")

    user = db.query(User).filter(User.id == int(user_id)).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user


# ---------------- Active User ----------------

def active_user_required(
    current_user: User = Depends(get_current_user)
):

    if not current_user.is_active:
        raise HTTPException(
            status_code=403,
            detail="User is inactive"
        )

    return current_user


# ---------------- Admin Only ----------------

def admin_required(
    current_user: User = Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return current_user
