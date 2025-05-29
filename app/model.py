from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

# Define the Post model
class Post(SQLModel, table=True):
    __tablename__ = "posts"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    published: bool = Field(default=True, nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    owner_id: Optional[int] = Field(default=None, foreign_key="users.id", ondelete="CASCADE")
    owner: Optional["User"] = Relationship(back_populates="posts")
    votes: List["Vote"] = Relationship(back_populates="post")

    class Config:
        orm_mode = True

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    posts: List["Post"] = Relationship(back_populates="owner")
    votes: List["Vote"] = Relationship(back_populates="user")


    class Config:
        orm_mode = True

class Vote(SQLModel, table=True):
    __tablename__ = "votes"

    post_id: int = Field(foreign_key="posts.id", primary_key=True, ondelete="CASCADE")
    user_id: int = Field(foreign_key="users.id", primary_key=True, ondelete="CASCADE")

    post: Optional[Post] = Relationship(back_populates="votes")
    user: Optional[User] = Relationship(back_populates="votes")
