from app.database.models import ActivityLog
from datetime import datetime

class LogService:

    def __init__(self, repo):
        self.repo = repo

    def create_log(
        self,
        user_id: int,
        action: str,
        description: str = ""
    ):

        log = ActivityLog(
            user_id=user_id,
            action=action,
            description=description,
            created_at=datetime.utcnow()
        )

        return self.repo.create(log)

    # ------------------------
    # All Logs
    # ------------------------
    def get_all(self):

        return self.repo.get_all()

    # ------------------------
    # User Logs
    # ------------------------
    def get_user_logs(self, user_id):

        return self.repo.get_by_user(user_id)