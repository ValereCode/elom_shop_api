"""Authentication router."""
from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Form
from app.jwt import create_access_token, create_refresh_token
from app.models.auth import RefreshToken
from app.models.user import User, UserAuth
from app.utils.password import verify_password



router = APIRouter(prefix="/auth", tags=["Authentification"])


@router.post("")
async def login(user_credentials: Annotated[UserAuth, Form()]):
    """Authenticate and returns the user's JWT."""
    user = await User.by_email(user_credentials.email)
    if user is None or not verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Bad email or password")
    if user.email_confirmed_at is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email is not yet verified")
    access_token = create_access_token(user.jwt_subject)
    refresh_token = create_refresh_token(user.jwt_subject)
    return RefreshToken(access_token=access_token, refresh_token=refresh_token)


# @router.post("/refresh")
# async def refresh(
#     auth: JwtAuthorizationCredentials = Security(refresh_security)
# ) -> AccessToken:
#     """Return a new access token from a refresh token."""
#     access_token = create_access_token(auth.subject)
#     return AccessToken(access_token=access_token)