from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, status

from app.models.category import Category
from app.models.user import UserOut
from app.jwt import get_current_user

router = APIRouter(prefix='/category', tags=["Catégories de produits"])

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_category(category: Category, current_user: UserOut = Depends(get_current_user)):
    await Category.insert_one(category)


@router.get('/{id}', response_model=Category, status_code=status.HTTP_200_OK)
async def get_category(id: PydanticObjectId):
    category = await Category.get(id)
    return category

@router.get('/', response_model=Category, status_code=status.HTTP_200_OK)
async def get_category():
    category = await Category.fing()
    return category

@router.put('/{id}', status_code=status.HTTP_200_OK)
async def update_category(id: PydanticObjectId, new_category: Category):
    category = await Category.get(id)
    await category.set({
        "name": new_category.name,
        "description": new_category.description
    })


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(id: PydanticObjectId):
    category = await Category.get(id)
    category.delete()