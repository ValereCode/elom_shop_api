from beanie import Document
from typing import Optional
from pydantic import Field
from datetime import datetime
from .product import Product
from .user import User
from beanie import Link


class Review(Document):
    product: Link[Product]
    user: Link[User]
    rating: int
    comment: Optional[str] = None
    review_date: datetime = Field(default_factory=datetime.now, alias="reviewDate")

    class Settings:
        name = "reviews"
