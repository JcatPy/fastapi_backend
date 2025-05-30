from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel
from pydantic import EmailStr, BaseModel
from pydantic import conint

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

class Vote_s(SQLModel):
    post_id: int
    dir: conint(ge=0, le=1)  # 0 or 1, where 1 means upvote and 0 means downvote

    class Config:
        orm_mode = True

class PostWithVotes(SQLModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    owner_id: Optional[int]
    votes: int  # This is the additional field from aggregation

    class Config:
        orm_mode = True


