from beanie import Document
from typing import List
from pydantic import Field
from bson import ObjectId
from datetime import datetime
from .cart_item import CartItem

class Cart(Document):
    user_id: ObjectId = Field(..., alias="userId")
    items: List[CartItem] = []
    creation_date: datetime = Field(default_factory=datetime.now, alias="creationDate")

    class Settings:
        name = "carts"

    class Config:
        arbitrary_types_allowed = True