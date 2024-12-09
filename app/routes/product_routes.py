from fastapi import APIRouter

from app.models.product import Product

router = APIRouter(prefix='/product', tags=['Produits'])

@router.post('/create')
async def create_product(product: Product):
    await Product.insert_one(product)
