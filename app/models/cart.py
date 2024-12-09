from beanie import Document, Link
from typing import List
from pydantic import Field
from datetime import datetime
from .cart_item import CartItem
from .user import User


class Cart(Document):
    user: Link[User]
    items: List[CartItem] = []
    creation_date: datetime = Field(default_factory=datetime.now, alias="creationDate")

    class Settings:
        name = "carts"

    class Config:
        arbitrary_types_allowed = True