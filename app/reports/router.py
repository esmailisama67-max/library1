from fastapi import APIRouter
from fastapi import Depends

from app.database.session import get_db

from app.auth.dependencies import admin_required

from app.reports.repository import ReportRepository

from app.reports.service import ReportService

from app.reports.schemas import DashboardResponse

router = APIRouter(
    prefix="/reports",
    tags=["Reports"] )

def get_report_service(db=Depends(get_db)):

    repo = ReportRepository(db)

    return ReportService(repo)

@router.get( "/dashboard",
    response_model=DashboardResponse )
def dashboard(

    admin=Depends(admin_required),

    service: ReportService = Depends(get_report_service)

):

    return service.dashboard()