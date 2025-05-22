from fastapi import APIRouter, Depends, HTTPException, FastAPI, status, Response
from sqlmodel import Session
from ..database import get_session
from ..model import User
from ..Schemas import UserCreate, UserOut
from ..utils import hash_password

router = APIRouter()

@router.post("/users", response_model=UserOut)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    hashed_password = hash_password(user.password)
    new_user = User(**user.dict(), password=hashed_password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@router.get("/users/{user_id}", response_model=UserOut)
def read_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user