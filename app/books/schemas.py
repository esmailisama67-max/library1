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

    total_copies:Optional[int] = Field(default=1, ge=1)


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
    total_copies: Optional[int] = None
    
# ----------------------
# Response Model
# ----------------------
class BookResponse(BaseModel):
    id:Optional[int]
    title: str
    isbn: str
    author: str
    publisher: Optional[str]
    publication_year: Optional[int]
    category: Optional[str]
    description: Optional[str]
    total_copies:Optional[int] = None
    available_copies:Optional[int] = None

    class Config:
        from_attributes = True
        

class BookOut(BaseModel):
    id:Optional[int] = None
    title: str
    isbn: str
    author: str
    publisher: str
    publication_year:Optional[int] = None
    category: str
    description: str
    
    total_copies:Optional[int] = None
    available_copies:Optional[int] = None

    class Config:
        from_attributes = True  