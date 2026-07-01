from sqlalchemy import select , or_
from app.database.models import Book
from typing import Optional

class BookRepository:

    def __init__(self, db):
        self.db = db

    # -------------------------
    # Create Book
    # -------------------------
    def create(self, book: Book):
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    # -------------------------
    # Get by ID
    # -------------------------
    def get_by_id(self, book_id: int):
        stmt = select(Book).where(Book.id == book_id)
        return self.db.execute(stmt).scalar_one_or_none()

    # -------------------------
    # Get all (pagination)
    # -------------------------
def get_all(
    self,
    skip: int = 0,
    limit: int = 10,
    category: Optional[str] = None,
    author: Optional[str] = None,
    sort_by: str = "id",
    order: str = "asc"
):

    stmt = select(Book)

    # ---------------------
    # Filters
    # ---------------------
    if category:
        stmt = stmt.where(Book.category == category)

    if author:
        stmt = stmt.where(Book.author == author)

    # ---------------------
    # Sorting
    # ---------------------
    if hasattr(Book, sort_by):
        column = getattr(Book, sort_by)

        if order == "desc":
            column = column.desc()
        else:
            column = column.asc()

        stmt = stmt.order_by(column)

    # ---------------------
    # Pagination
    # ---------------------
    stmt = stmt.offset(skip).limit(limit)

    return self.db.execute(stmt).scalars().all()

    # -------------------------
    # Delete
    # -------------------------
def delete(self, book: Book):
        self.db.delete(book)
        self.db.commit()

    # -------------------------
    # Update (simple)
    # -------------------------
def update(self):
        self.db.commit()
        
    #-------------------
    #search books ------
    #------------------
def search_books(
    self,
    title: Optional[str] = None,
    author: Optional[str] = None,
    isbn: Optional[str] = None,
    category: Optional[str] = None
):
    stmt = select(Book)

    conditions = []

    if title:
        conditions.append(Book.title.ilike(f"%{title}%"))

    if author:
        conditions.append(Book.author.ilike(f"%{author}%"))

    if isbn:
        conditions.append(Book.isbn.ilike(f"%{isbn}%"))

    if category:
        conditions.append(Book.category.ilike(f"%{category}%"))

    if conditions:
        stmt = stmt.where(or_(*conditions))

    return self.db.execute(stmt).scalars().all()