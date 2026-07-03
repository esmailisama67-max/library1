from sqlalchemy import func, select
from datetime import datetime
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
    
    # -----------------------
    # Books Report
    # -----------------------
    def books_report(self):

        return {

            "total_books": self.total_books(),

            "available_books": self.available_books(),

            "borrowed_books": self.borrowed_books()

        }
        
    # -----------------------
    # Users Report
    # -----------------------
    def users_report(self):

        inactive_users = self.total_users() - self.active_users()

        return {

            "total_users": self.total_users(),

            "active_users": self.active_users(),

            "inactive_users": inactive_users

        }
        # -----------------------
    # Borrow Report
    # -----------------------
    def borrow_report(self):

        total = self.db.execute(

            select(func.count(BorrowRecord.id))

        ).scalar()

        borrowed = self.borrowed_books()

        returned = total - borrowed

        return {

            "total_records": total,

            "borrowed": borrowed,

            "returned": returned

        }
        
        # -----------------------
# Overdue Report
# -----------------------
def overdue_report(self):

    overdue = self.db.execute(

        select(func.count(BorrowRecord.id))

        .where(

            BorrowRecord.status == "borrowed",

            BorrowRecord.due_date < datetime.utcnow()

        )

    ).scalar()

    return {

        "overdue_books": overdue
    }