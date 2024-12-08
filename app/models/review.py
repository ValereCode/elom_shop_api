from beanie import Document
from typing import Optional
from pydantic import Field
from bson import ObjectId
from datetime import datetime


class Review(Document):
    product_id: ObjectId = Field(..., alias="productId")
    user_id: ObjectId = Field(..., alias="userId")
    rating: int
    comment: Optional[str] = None
    review_date: datetime = Field(default_factory=datetime.now, alias="reviewDate")

    class Settings:
        name = "reviews"
