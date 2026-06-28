from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.database.session import SessionLocal 
from app.database.models import User 
from app.auth.jwt_handler import SECRET_KEY, ALGORITHM

from app.database.session import get_db
from app.database.models import User
from app.auth.jwt_handler import verify_token



# ---------------- OAuth2 ----------------

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


# ---------------- Current User ----------------

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    print("TOKEN =", token)
    
    payload = verify_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    user = (
        db.query(User)
        .filter(User.id == int(user_id))
        .first()
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
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
