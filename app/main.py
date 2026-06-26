from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.database.session import get_db
from app.auth.test_routes import router as test_router


app = FastAPI()

app.include_router(auth_router)

app.include_router(test_router)