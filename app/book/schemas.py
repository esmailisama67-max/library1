from pydantic import BaseModel
from typing import Optional


class BookCreate(BaseModel):
    title: str
    isbn: str
    author: str
    publisher: str
    publication_year: Optional[int] = None
    category: Optional[str] = None
    description: Optional[str] = None
    total_copies: Optional[int] = 1


class BookResponse(BaseModel):
    id: int
    title: str
    isbn: str
    author: str
    publisher: str
    publication_year: Optional[int]
    category: Optional[str]
    description: Optional[str]
    total_copies: int
    available_copies: int

    class Config:
        from_attributes = True