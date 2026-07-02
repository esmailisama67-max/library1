from pydantic import BaseModel


class DashboardResponse(BaseModel):

    total_users: int

    total_books: int

    borrowed_books: int

    available_books: int

    active_users: int