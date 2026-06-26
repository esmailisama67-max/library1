from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# -------------------------
# Register
# -------------------------
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=32
    )


# -------------------------
# Login
# -------------------------
class UserLogin(BaseModel):
    username_or_email: str
    password: str


# -------------------------
# User Response
# -------------------------
class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    role: str
    is_active: bool

    class Config:
        from_attributes = True


# -------------------------
# Update User (Admin)
# -------------------------
class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None


# -------------------------
# Update Profile
# -------------------------
class UserProfileUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None


# -------------------------
# Change Password
# -------------------------
class ChangePassword(BaseModel):
    old_password: str

    new_password: str = Field(
        min_length=8,
        max_length=32
    )


# -------------------------
# Token Response
# -------------------------
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


# -------------------------
# Refresh Token Request
# -------------------------
class RefreshTokenRequest(BaseModel):
    refresh_token: str


# -------------------------
# Message Response
# -------------------------
class MessageResponse(BaseModel):
    message: str