from sqlalchemy import select

from app.database.models import ActivityLog


class LogRepository:

    def __init__(self, db):
        self.db = db

    # ------------------------
    # Create Log
    # ------------------------
    def create(self, log):

        self.db.add(log)

        self.db.commit()

        self.db.refresh(log)

        return log

    # ------------------------
    # Get All Logs
    # ------------------------
    def get_all(self):

        stmt = (
            select(ActivityLog)
            .order_by(ActivityLog.created_at.desc())
        )

        return self.db.execute(stmt).scalars().all()

    # ------------------------
    # Logs By User
    # ------------------------
    def get_by_user(self, user_id):

        stmt = (
            select(ActivityLog)
            .where(ActivityLog.user_id == user_id)
            .order_by(ActivityLog.created_at.desc())
        )

        return self.db.execute(stmt).scalars().all()