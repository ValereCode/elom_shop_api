"""Authentication router."""

from fastapi import APIRouter, HTTPException, status

from app.jwt import create_access_token, create_refresh_token
from app.models.auth import RefreshToken
from app.models.user import User, UserAuth
from app.utils.password import verify_password


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("")
async def login(user_auth: UserAuth):
    """Authenticate and returns the user's JWT."""
    print("HIIIII")
    user = await User.by_email(user_auth.email)
    print(f"HIIIIIIIIIIII  {user}")
    if user is None or verify_password(user_auth.password, user.password):
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