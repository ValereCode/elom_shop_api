from pydantic import BaseModel
from pydantic import Field
from .product import Product
from beanie import Link

class OrderItem(BaseModel):
    product: Link[Product]
    quantity: int
    unit_price: float = Field(..., alias="unitPrice")
