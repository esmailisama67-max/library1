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
        
    # -----------------------
    # Books Report
    # -----------------------
    def books_report(self):

        return self.repo.books_report()
    
    # -----------------------
    # Users Report
    # -----------------------
    def users_report(self):

        return self.repo.users_report()
    
    # -----------------------
    # Borrow Report
    # -----------------------
    def borrow_report(self):

        return self.repo.borrow_report()
    
    # -----------------------
    # Overdue Report
    # -----------------------
    def overdue_report(self):

        return self.repo.overdue_report()
    
    