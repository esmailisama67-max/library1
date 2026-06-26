from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.books.schemas import (
    BookCreate,
    BookUpdate,
    BookResponse,
    BookListResponse
)
from app.books.service import BookService

from app.auth.dependencies import (
    get_current_user,
    admin_required
)

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.post(
    "",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED
)
def create_book(
        book_data: BookCreate,
        db: Session = Depends(get_db),
        current_user=Depends(admin_required)
):
    service = BookService(db)
    return service.create_book(book_data)


@router.get(
    "",
    response_model=BookListResponse
)
def get_books(
        page: int = Query(1, ge=1),
        size: int = Query(10, ge=1, le=100),

        title: Optional[str] = None,
        author: Optional[str] = None,
        category: Optional[str] = None,
        publisher: Optional[str] = None,
        publication_year: Optional[int] = None,

        sort_by: str = "id",
        sort_order: str = "asc",

        db: Session = Depends(get_db)
):
    service = BookService(db)

    return service.get_books(
        page=page,
        size=size,
        title=title,
        author=author,
        category=category,
        publisher=publisher,
        publication_year=publication_year,
        sort_by=sort_by,
        sort_order=sort_order
    )


@router.get(
    "/search",
    response_model=BookListResponse
)
def search_books(
        title: Optional[str] = None,
        author: Optional[str] = None,
        isbn: Optional[str] = None,
        category: Optional[str] = None,
        db: Session = Depends(get_db)
):
    service = BookService(db)

    return service.search_books(
        title=title,
        author=author,
        isbn=isbn,
        category=category
    )


@router.get(
    "/categories",
    response_model=list[str]
)
def get_categories(
        db: Session = Depends(get_db)
):
    service = BookService(db)
    return service.get_categories()


@router.get(
    "/{book_id}",
    response_model=BookResponse
)
def get_book(
        book_id: int,
        db: Session = Depends(get_db)
):
    service = BookService(db)
    return service.get_book(book_id)


@router.put(
    "/{book_id}",
    response_model=BookResponse
)
def update_book(
        book_id: int,
        book_data: BookUpdate,
        db: Session = Depends(get_db),
        current_user=Depends(admin_required)
):
    service = BookService(db)

    return service.update_book(
        book_id,
        book_data
    )


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_book(
        book_id: int,
        db: Session = Depends(get_db),
        current_user=Depends(admin_required)
):
    service = BookService(db)

    service.delete_book(book_id)