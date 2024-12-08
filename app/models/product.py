from beanie import Document
from typing import Optional
from pydantic import Field
from bson import ObjectId

class Product(Document):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    image: Optional[str] = None
    category_id: ObjectId = Field(..., alias="categoryId")

    class Settings:
        name = "products"
