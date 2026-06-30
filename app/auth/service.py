from app.users.repository import UserRepository
from app.database.models import User
from app.auth.security import hash_password , verify_password


class AuthService:

    def __init__(self, db):
        self.repository = UserRepository(db)

    def register(self, data):

        if self.repository.get_by_email(data.email):
            raise Exception("Email already exists")

        if self.repository.get_by_username(data.username):
            raise Exception("Username already exists")

        user = User(
            first_name=data.first_name,
            last_name=data.last_name,
            username=data.username,
            email=data.email,
            password_hash=hash_password(data.password)
        )

        return self.repository.create(user)