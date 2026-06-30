from app.database.models import ActivityLog
from datetime import datetime

class LogService:

    def __init__(self, db):
        self.db = db

    def create_log(self, user_id: int, action: str, description: str = ""):
        log = ActivityLog(
            user_id=user_id,
            action=action,
            description=description,
            created_at=datetime.utcnow()
        )

        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)
        return log