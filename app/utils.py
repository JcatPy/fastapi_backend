from passlib.context import CryptContext

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto") # Password hashing context

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    """
    return pwd.hash(password)

def verify(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.
    """
    return pwd.verify(plain_password, hashed_password)

