from fastapi import HTTPException
from app.database.models import Book


class BookService:

    def __init__(self, repo):
        self.repo = repo

    # -------------------------
    # Create Book
    # -------------------------
    def create_book(self, data):
        if data.total_copies <= 0:
            raise HTTPException(400, "Total copies must be greater than 0")

        book = Book(
            title=data.title,
            isbn=data.isbn,
            author=data.author,
            publisher=data.publisher,
            publication_year=data.publication_year,
            category=data.category,
            description=data.description,
            total_copies=data.total_copies,
            available_copies=data.total_copies
        )

        return self.repo.create(book)

    # -------------------------
    # Get books
    # -------------------------
    def get_books(
        self,
        skip,
        limit,
        category=None,
        author=None,
        sort_by="id",
        order="asc"
    ):
        return self.repo.get_all(
            skip=skip,
            limit=limit,
            category=category,
            author=author,
            sort_by=sort_by,
            order=order
        )

    # -------------------------
    # Get single book
    # -------------------------
    def get_book(self, book_id: int):

        book = self.repo.get_by_id(book_id)

        if not book:
            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )

        return book
   
    # -------------------------
    # Delete book (rule check)
    # -------------------------
    def delete_book(self, book_id: int):

        book = self.repo.get_by_id(book_id)

        if not book:
            raise HTTPException(404, "Book not found")

        # ❗ Rule: اگر نسخه موجود کمتر از total باشد یعنی امانت رفته
        if book.available_copies < book.total_copies:
            raise HTTPException(
                status_code=400,
                detail="Book cannot be deleted because it is currently borrowed"
            )

        self.repo.delete(book)

        return {"message": "Book deleted successfully"}

    # -------------------------
    # Update book
    # -------------------------
    def update_book(self, book_id: int, data):

        book = self.repo.get_by_id(book_id)

        if not book:
            raise HTTPException(404, "Book not found")

        for key, value in data.dict(exclude_unset=True).items():
            setattr(book, key, value)

        self.repo.update()

        return book
    
    def search_books(
        self,
        title=None,
        author=None,
        isbn=None,
        category=None
    ):
        return self.repo.search_books(
            title,
            author,
            isbn,
            category
        )