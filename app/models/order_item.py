from pydantic import BaseModel
from bson import ObjectId
from pydantic import Field

class OrderItem(BaseModel):
    product_id: ObjectId = Field(..., alias="productId")
    quantity: int
    unit_price: float = Field(..., alias="unitPrice")
