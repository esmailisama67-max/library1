from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column , Integer , String , DateTime , Boolean , Text
from sqlalchemy import ForeignKey
from datetime import datetime

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String , nullable= False)
    last_name = Column(String , nullable= False)

    username = Column(String, unique=True , index=True, nullable=False)
    email = Column(String, unique=True ,index=True, nullable=False)

    password_hash = Column (String , nullable= False)

    role = Column(String, default="user")

    is_active = Column(Boolean, default=True)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime , default=datetime.utcnow)
    updated_at = Column(DateTime , default=datetime.utcnow, onupdate=datetime.utcnow)
        


class Book(Base):
        __tablename__ = "books"

        id = Column(Integer, primary_key=True , index = True)

        title = Column(String , nullable= False)
        
        isbn = Column( String, unique=True, nullable=False)

        author = Column(String , nullable= False)
        
        publisher = Column(String , nullable= False)

        publication_year = Column(Integer, nullable=True)

        category = Column(String(100), nullable=True)

        description = Column(Text, nullable=True)

        total_copies = Column(Integer, default=1)

        available_copies = Column(Integer, default=1)
        
        created_at = Column( DateTime, default=datetime.utcnow )
        
        updated_at = Column( DateTime, default=datetime.utcnow, onupdate=datetime.utcnow )

class BorrowRecord(Base):
    __tablename__ = "borrow_records"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    book_id = Column(Integer, ForeignKey("books.id"))

    borrow_date = Column(DateTime, default=datetime.utcnow )

    due_date = Column(DateTime)

    return_date = Column(DateTime)

    status = Column( String, default="borrowed")

class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    token = Column(String, nullable=False, unique=True)

    expires_at = Column(DateTime , default= datetime.utcnow , nullable=False )

    created_at = Column(DateTime , default= datetime.utcnow)

    is_revoked = Column(Boolean, default=False )
    


class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    action = Column(String)

    description = Column(Text)

    created_at = Column(
    DateTime,
    default=datetime.utcnow )