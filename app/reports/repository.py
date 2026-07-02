from sqlalchemy import func, select

from app.database.models import User
from app.database.models import Book
from app.database.models import BorrowRecord

class ReportRepository:

    def __init__(self, db):
        self.db = db
        
# -----------------------
# Total Users
# -----------------------

    def total_users(self):

        stmt = select(func.count(User.id))

        return self.db.execute(stmt).scalar()
    # -----------------------
    # Total Books
    # -----------------------

    def total_books(self):

        stmt = select(func.count(Book.id))

        return self.db.execute(stmt).scalar()
    
    # -----------------------
    # Borrowed Books
    # -----------------------

    def borrowed_books(self):

        stmt = (

            select(func.count(BorrowRecord.id))

            .where(BorrowRecord.status == "borrowed")

        )

        return self.db.execute(stmt).scalar()
    
    # -----------------------
    # Available Books
    # -----------------------

    def available_books(self):

        stmt = select(func.sum(Book.available_copies))

        result = self.db.execute(stmt).scalar()

        return result or 0
    
    # -----------------------
    # Active Users
    # -----------------------

    def active_users(self):

        stmt = (

            select(func.count(User.id))

            .where(User.is_active == True)

        )

        return self.db.execute(stmt).scalar()
    
    