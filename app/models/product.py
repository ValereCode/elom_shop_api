from beanie import Document
from typing import Optional
from beanie import Link
from .category import Category


class Product(Document):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    image: Optional[str] = None
    category: Link[Category]

    class Settings:
        name = "products"
