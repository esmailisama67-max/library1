from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.auth.test_routes import router as test_router
from app.users.router import router as user_router
from app.database.connection import engine
from app.database.models import Base
from app.books.router import router as books_router
from app.borrows.router import router as borrow_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)

app.include_router(test_router)

app.include_router(books_router)

app.include_router(borrow_router)

app.include_router(user_router)

#موقت
#print(app.routes)