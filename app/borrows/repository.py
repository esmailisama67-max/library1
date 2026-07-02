from sqlalchemy import select

from app.database.models import BorrowRecord

from datetime import datetime

class BorrowRepository:

    def __init__(self, db):
        self.db = db

    # ---------------------
    # Create Borrow
    # ---------------------
    def create(self, borrow: BorrowRecord):

        self.db.add(borrow)

        self.db.commit()

        self.db.refresh(borrow)

        return borrow

    # ---------------------
    # Get By ID
    # ---------------------
    def get_by_id(self, borrow_id: int):

        stmt = select(BorrowRecord).where(
            BorrowRecord.id == borrow_id
        )

        return self.db.execute(stmt).scalar_one_or_none()

    # ---------------------
    # Update
    # ---------------------
    def update(self):

        self.db.commit()

    # ---------------------
    # User Borrows
    # ---------------------
    def get_user_borrows(self, user_id: int):

        stmt = select(BorrowRecord).where(
            BorrowRecord.user_id == user_id
        )

        return self.db.execute(stmt).scalars().all()

    # ---------------------
    # Borrow History
    # ---------------------
    def get_history(self, user_id: int):

        stmt = (
            select(BorrowRecord)
            .where(BorrowRecord.user_id == user_id)
            .order_by(BorrowRecord.borrow_date.desc())
        )

        return self.db.execute(stmt).scalars().all()

    # ---------------------
    # All Borrows
    # ---------------------
    def get_all(self):

        stmt = select(BorrowRecord)

        return self.db.execute(stmt).scalars().all()
    
    def get_active_user_books(
    self,
    user_id: int ):

        stmt = select(BorrowRecord).where(

            BorrowRecord.user_id == user_id,

            BorrowRecord.status == "borrowed"

        )

        return self.db.execute(
            stmt
        ).scalars().all()
        
    # ---------------------
    # Overdue Books
    # ---------------------
    def get_overdue(self):

        stmt = select(BorrowRecord).where(

            BorrowRecord.status == "borrowed",

            BorrowRecord.due_date < datetime.utcnow()

        )

        return self.db.execute(stmt).scalars().all()