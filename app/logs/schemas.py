from datetime import datetime

from pydantic import BaseModel


class LogResponse(BaseModel):

    id: int

    user_id: int

    action: str

    description: str

    created_at: datetime

    class Config:
        from_attributes = True