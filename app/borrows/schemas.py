from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# -------------------------
# Borrow Book
# -------------------------
class BorrowCreate(BaseModel):
    book_id: int


# -------------------------
# Return Book
# -------------------------
class ReturnBook(BaseModel):
    borrow_id: int


# -------------------------
# Borrow Response
# -------------------------
class BorrowResponse(BaseModel):

    id: int

    user_id: int

    book_id: int

    borrow_date: datetime

    due_date: datetime

    return_date: Optional[datetime]

    status: str

    class Config:
        from_attributes = True