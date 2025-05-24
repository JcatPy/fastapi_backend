from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from ..database import get_session
from ..model import User
from ..utils import verify
from ..oauth2 import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=["auth"])

@router.post("/login")
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    print("✅ Login request received")
    # Get the user by email (username in OAuth2PasswordRequestForm)
    statement = select(User).where(User.email == user_credentials.username)
    user = session.exec(statement).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    if not verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    # Generate JWT
    access_token = create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
