from datetime import datetime, timedelta

from fastapi import HTTPException , Depends

from app.database.models import BorrowRecord

from app.database.session import get_db

from app.books.repository import BookRepository

from app.borrows.repository import BorrowRepository

class BorrowService:

    def __init__(self, borrow_repo, book_repo):
        self.borrow_repo = borrow_repo
        self.book_repo = book_repo
        
    def borrow_book(self, user_id: int, book_id: int):

        book = self.book_repo.get_by_id(book_id)

        if not book:
            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )

        if book.available_copies <= 0:
            raise HTTPException(
                status_code=400,
                detail="Book is not available"
            )

        borrow = BorrowRecord(

            user_id=user_id,

            book_id=book.id,

            borrow_date=datetime.utcnow(),

            due_date=datetime.utcnow() + timedelta(days=14),

            status="borrowed"
        )

        book.available_copies -= 1

        self.book_repo.update()

        return self.borrow_repo.create(borrow)
            
    def my_books( self,user_id
):

        return self.borrow_repo.get_active_user_books( user_id)
        
    
    def return_book(
    self,
    borrow_id: int
):

        borrow = self.borrow_repo.get_by_id(
            borrow_id )

        if not borrow:

            raise HTTPException(
                404,
                "Borrow not found" )

        if borrow.status == "returned":

            raise HTTPException(
                400,
                "Book already returned")

        book = self.book_repo.get_by_id(
            borrow.book_id)

        borrow.return_date = datetime.utcnow()

        borrow.status = "returned"

        book.available_copies += 1

        self.book_repo.update()

        self.borrow_repo.update()

        return borrow
    
    # ---------------------
    # Borrow History
    # ---------------------
    def history(self, user_id: int):

        return self.borrow_repo.get_history(user_id)
    
    # ---------------------
    # All Borrows
    # ---------------------
    def get_all(self):

        return self.borrow_repo.get_all()
    # ---------------------
    # Overdue
    # ---------------------
    def overdue(self):

        return self.borrow_repo.get_overdue()
    
def get_borrow_service(db=Depends(get_db)):

    borrow_repo = BorrowRepository(db)

    book_repo = BookRepository(db)

    return BorrowService(
        borrow_repo,
        book_repo
    )