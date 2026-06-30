from sqlalchemy.orm import Session
from datetime import datetime
from app.database.models import User
from sqlalchemy import select

class UserRepository:

    def __init__(self, db: Session):
        self.db = db
    def get_all(
        self,
        skip: int = 0,
        limit: int = 10
    ):

        stmt = (
            select(User)

            .where(User.deleted_at == None)

            .offset(skip)

            .limit(limit)
        )

        return self.db.execute(stmt).scalars().all()
    
    def get_by_username(self, username: str):

        return (
            self.db.query(User)
            .filter(User.username == username)
            .first()
        )
    def get_by_email(self, email: str):

        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )


    def create(self, user: User):

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def get_all(
    self,
    skip: int = 0,
    limit: int = 10
):

        return (
        self.db.query(User)

        .filter(User.deleted_at == None)

        .offset(skip)

        .limit(limit)

        .all()
    )

def get_by_id( self, user_id: int ):

    return (

        self.db.query(User)

        .filter(
            User.id == user_id,
            User.deleted_at == None )

        .first()
    )
    
def update( self, user, data ):

    user.first_name = data.first_name

    user.last_name = data.last_name

    user.email = data.email

    self.db.commit()

    self.db.refresh(user)

    return user

def soft_delete(
    self,
    user
):

    user.deleted_at = datetime.utcnow()

    self.db.commit()
    
