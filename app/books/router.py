from fastapi import APIRouter, Depends, Query
from app.books.schemas import BookCreate, BookUpdate, BookResponse
from app.books.service import BookService
from app.database.session import get_db
from app.auth.dependencies import admin_required
from app.books.repository import BookRepository
from typing import Optional


router = APIRouter(prefix="/books", tags=["Books"])


# Dependency
def get_book_service(db=Depends(get_db)):
    
    return BookService(BookRepository(db))


# -------------------------
# Create Book (Admin)
# -------------------------
@router.post("", response_model=BookResponse)
def create_book(
    data: BookCreate,
    service: BookService = Depends(get_book_service),
    user=Depends(admin_required) ):
    return service.create_book(data)


# -------------------------
# Get all books (pagination)
# -------------------------

@router.get("", operation_id="books_get_all")

def get_books(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),

    category: Optional[str] = None,
    author: Optional[str] = None,

    sort_by: str = "id",
    order: str = "asc",

    service: BookService = Depends(get_book_service)
):
    return service.get_books(
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
@router.get("/{book_id}", response_model=BookResponse)
def get_book(
    book_id: int,
    service: BookService = Depends(get_book_service)
):
    return service.get_book(book_id)


# -------------------------
# Update book (Admin)
# -------------------------
@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    data: BookUpdate,
    service: BookService = Depends(get_book_service),
    user=Depends(admin_required)
):
    return service.update_book(book_id, data)


# -------------------------
# Delete book (Admin)
# -------------------------
@router.delete("/{book_id}")
def delete_book(
    book_id: int,
    service: BookService = Depends(get_book_service),
    user=Depends(admin_required)
):
    return service.delete_book(book_id)
@router.get("/search")
def search_books(
    title: Optional[str] = None,
    author: Optional[str] = None,
    isbn: Optional[str] = None,
    category: Optional[str] = None,
    service: BookService = Depends(get_book_service)
):
    return service.search_books(
        title,
        author,
        isbn,
        category
    )
    