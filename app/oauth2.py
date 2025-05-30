from jose import jwt, JWTError
from datetime import datetime, timedelta
from .Schemas import TokenData
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlmodel import Session
from .database import get_session
from .model import User
from .config import settings

SECRET_KEY = f"{settings.secret_key}"
ALGORITHM = f"{settings.algorithm}"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Create a token
def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Verify the access token
def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=str(id))
    except JWTError:
        raise credentials_exception
    return token_data

# Get the current user from the token
def get_current_user(token: str= Depends(oauth2_scheme), session: Session = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = verify_access_token(token, credentials_exception)
    user = session.get(User, token_data.id)
    return user if user else None