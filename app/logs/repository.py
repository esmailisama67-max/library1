from app.database.models import ActivityLog

class LogRepository:

    def __init__(self, db):
        self.db = db

    def create(self, log: ActivityLog):
        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)
        return log