from passlib.context import CryptContext

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto") # Password hashing context

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    """
    return pwd.hash(password)

