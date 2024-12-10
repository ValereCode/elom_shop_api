from fastapi import APIRouter, Depends

from app.models.category import Category
from app.models.user import UserOut
from app.jwt import get_current_user

router = APIRouter(prefix='/category', tags=["Catégories de produits"])

@router.post('/create')
async def create_category(category: Category, current_user: UserOut = Depends(get_current_user)):
    await Category.insert_one(category)


@router.get('/read')
async def get_category():
    pass

@router.put('/update')
async def update_category():
    pass