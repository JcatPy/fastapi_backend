from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel
from pydantic import EmailStr

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

class UserOut(SQLModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class Userlogin(SQLModel):
    email: EmailStr
    password: str