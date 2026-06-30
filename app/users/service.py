from fastapi import HTTPException , Depends
from app.database.session import get_db
from app.database.models import User
from app.users.repository import UserRepository
from app.auth.security import hash_password, verify_password 
from app.auth.jwt_handler import create_access_token, create_refresh_token


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
            password_hash=hash_password( data.password ),
            role=data.role
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
def get_users(
    self, skip, limit ):
    return self.repo.get_all(
        skip, limit
    )
    
def delete_user(
    self,
    user_id
):

    user = self.repo.get_by_id(
        user_id
    )

    if not user:

        raise HTTPException(
            404,
            "User not found"
        )

    self.repo.soft_delete( user )
    
def update_profile(
    self,
    current_user,
    data
):
    current_user.first_name = data.first_name
    current_user.last_name = data.last_name
    current_user.email = data.email

    self.db.commit()
    self.db.refresh(current_user)

    return current_user
def change_password(
    self,
    current_user,
    data
):
    if not verify_password(
        data.old_password,
        current_user.password_hash
    ):
        raise HTTPException(
            status_code=400,
            detail="Old password is incorrect."
        )

    current_user.password_hash = hash_password(
        data.new_password
    )

    self.db.commit()

    return {
        "message": "Password changed successfully."
    }
    
def get_users(
    self,
    skip: int,
    limit: int
):
    return self.repo.get_all( skip, limit )

def get_user_service(db=Depends(get_db)):
    
    return UserService(db)