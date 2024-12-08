from pydantic import BaseModel
from bson import ObjectId
from pydantic import Field

class CartItem(BaseModel):
    product_id: ObjectId = Field(..., alias="productId")
    quantity: int
