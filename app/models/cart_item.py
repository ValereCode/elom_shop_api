from pydantic import BaseModel
from beanie import Link
from .product import Product


class CartItem(BaseModel):
    product: Link[Product]
    quantity: int
