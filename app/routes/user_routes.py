from fastapi import APIRouter, status
from app.models.user import User, UserOut
from app.utils.password import hash_password



router = APIRouter(prefix='/user',tags=['Utilisateurs'])

@router.post('', status_code=status.HTTP_201_CREATED, response_model= UserOut)
async def create_user(user: User):
    user.password = hash_password(user.password)
    new_user = User(**user.model_dump())
    await User.insert_one(new_user)
