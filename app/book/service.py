from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.books.repository import BookRepository
from app.books.schemas import BookCreate, BookUpdate

class BookService:

            def __init__(self, db: Session):
                self.repository = BookRepository(db)

            def create_book(
                self,
                book_data: BookCreate
        ):existing_book = self.repository.get_by_isbn(
            book_data.isbn
        )

        if existing_book:
            raise HTTPException(
                status_code=400,
                detail="ISBN already exists"
            )

        book = self.repository.create(book_data)

    return book

    #ef get_books(
               #self,
               #page: int,
               #size: int,
               #title: str = None,
               #author: str = None,
               #category: str = None,
               #publisher: str = None,
               #publication_year: int = None,
               #sort_by: str = "id",
               #sort_order: str = "asc"
       #):offset = (page - 1) * size

       #sort_by="publication_year"
       #sort_order="desc"

   #return {
           #"items": books,
           #"page": page,
           #"size": size,
           #"total": total }