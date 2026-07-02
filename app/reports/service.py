class ReportService:

    def __init__(self, repo):

        self.repo = repo

    # -------------------------
    # Dashboard
    # -------------------------
    def dashboard(self):

        return {

            "total_users": self.repo.total_users(),

            "total_books": self.repo.total_books(),

            "borrowed_books": self.repo.borrowed_books(),

            "available_books": self.repo.available_books(),

            "active_users": self.repo.active_users()

        }