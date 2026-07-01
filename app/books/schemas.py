from pydantic import BaseModel, Field
from typing import Optional


# ----------------------
# Create Book
# ----------------------
class BookCreate(BaseModel):
    title: str
    isbn: str
    author: str
    publisher: Optional[str] = None
    publication_year: Optional[int] = None
    category: Optional[str] = None
    description: Optional[str] = None

    total_copies: int = Field(default=1, ge=1)


# ----------------------
# Update Book
# ----------------------
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    publication_year: Optional[int] = None
    category: Optional[str] = None
    description: Optional[str] = None


# ----------------------
# Response Model
# ----------------------
class BookResponse(BaseModel):
    id: int
    title: str
    isbn: str
    author: str
    publisher: Optional[str]
    publication_year: Optional[int]
    category: Optional[str]
    description: Optional[str]
    total_copies: int
    available_copies: int

    class Config:
        from_attributes = True
  