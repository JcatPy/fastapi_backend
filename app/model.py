from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional
# Define the Post model
class Post(SQLModel, table=True):
    __tablename__ = "posts"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    published: bool = Field(default=True, nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    class Config:
        orm_mode = True

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    class Config:
        orm_mode = True
