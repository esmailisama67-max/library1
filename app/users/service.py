from fastapi import HTTPException

from app.database.models import User
from app.users.repository import UserRepository
from app.auth.security import (
    hash_password,
    verify_password
)
from app.auth.jwt_handler import (
    create_access_token,
    create_refresh_token
)


class UserService:

    def __init__(self, db):
        self.repo = UserRepository(db)


    def register(self, data):

        if self.repo.get_by_username(data.username):
            raise HTTPException(
                status_code=400,
                detail="Username already exists"
            )

        if self.repo.get_by_email(data.email):
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

        user = User(
            first_name=data.first_name,
            last_name=data.last_name,
            username=data.username,
            email=data.email,
            password_hash=hash_password(
                data.password
            )
        )

        return self.repo.create(user)


    def login(self, data):

        user = (
            self.repo.get_by_username(data.username_or_email)
            or
            self.repo.get_by_email(data.username_or_email)
)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )

        if not verify_password(
                data.password,
                user.password_hash
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )

        access_token = create_access_token(
            {
                "sub": str(user.id)
            }
        )

        refresh_token = create_refresh_token(
            {
                "sub": str(user.id)
            }
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }