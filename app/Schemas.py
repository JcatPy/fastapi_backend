from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel
from pydantic import EmailStr, BaseModel


class PostCreate(SQLModel):
    title: str
    content: str
    published: Optional[bool] = True

class PostUpdate(SQLModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None

class UserCreate(SQLModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class Userlogin(SQLModel):
    email: EmailStr
    password: str

class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    id: Optional[str] = None

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    owner_id: int
    owner: Optional[UserOut]  # nested user

    class Config:
        orm_mode = True

