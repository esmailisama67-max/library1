from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user

from app.borrows.schemas import BorrowCreate

from app.borrows.schemas import BorrowResponse

from app.borrows.service import ( BorrowService, get_borrow_service )

from app.borrows.schemas import ReturnBook

from typing import List

from app.auth.dependencies import admin_required 

router = APIRouter(

    prefix="/borrow",

    tags=["Borrow"]
)

@router.post(
    "",
    response_model=BorrowResponse
)
def borrow_book(

    data: BorrowCreate,

    current_user=Depends(get_current_user),

    service: BorrowService = Depends(
        get_borrow_service
    )

):

    return service.borrow_book(

        current_user.id,

        data.book_id
    )
    
@router.get(
    "/my-books", response_model=List[BorrowResponse]
)
def my_books(
    current_user=Depends(
        get_current_user ),
    service: BorrowService = Depends(
        get_borrow_service
    )

):

    return service.my_books(
        current_user.id
    )
    
@router.post(
    "/return",
    response_model=BorrowResponse
)
def return_book(

    data: ReturnBook,

    service: BorrowService = Depends(
        get_borrow_service
    )

):

    return service.return_book( data.borrow_id )

@router.get(
    "/history",
    response_model=List[BorrowResponse]
)
def borrow_history(
    current_user=Depends(get_current_user),
    service: BorrowService = Depends(get_borrow_service)
):
    return service.history(current_user.id)

@router.get("/all", response_model=List[BorrowResponse]
)
def all_borrows( admin =Depends(admin_required), service: BorrowService = Depends(get_borrow_service)
):
    return service.get_all()

@router.get(
    "/overdue",
    response_model=List[BorrowResponse]
)
def overdue(
    admin=Depends(admin_required),
    service: BorrowService = Depends(get_borrow_service) ):
    return service.overdue()