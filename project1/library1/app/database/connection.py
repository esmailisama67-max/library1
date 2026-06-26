from sqlalchemy import create_engine

# آدرس دیتابیس SQLite
DATABASE_URL = "sqlite:///library.db"

# ساخت Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)