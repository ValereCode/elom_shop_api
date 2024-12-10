"""Password utility functions."""
from passlib.context import CryptContext # type: ignore

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")   # Bcrypt is the default hashing algorithm

def hash_password(password: str):
    """This function should help us hashing our password with bcrypt"""
    return pwd_context.hash(password)

def verify_password(password, hashed_password):
    """This function will verify if the password the user type to login is his password"""
    return pwd_context.verify(password, hashed_password)