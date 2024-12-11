from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
import jwt
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer
from app import config
from app.models.auth import TokenData
from app.models.user import User



# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = config.settings.secret_key
ALGORITHM = config.settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = config.settings.access_token_expire_minutes

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict):
    to_encode = data.copy()
    # Par exemple, ajouter une durée de vie plus longue ou un champ spécifique
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES * 10)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credentials_exceptions):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        email: str = payload.get("username")
        if not email:
            raise credentials_exceptions
        token_data = TokenData(email=str(email))
        
    except InvalidTokenError:
        raise credentials_exceptions
    
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token = verify_access_token(token, credentials_exception)
    user = User.get(token.email)
    if user is None:
        raise credentials_exception

    return user