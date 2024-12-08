from beanie import Document
from typing import List
from pydantic import Field
from bson import ObjectId
from datetime import datetime
from enum import Enum
from .order_item import OrderItem

class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class Order(Document):
    user_id: ObjectId = Field(..., alias="userId")
    items: List[OrderItem]
    order_date: datetime = Field(default_factory=datetime.now, alias="orderDate")
    status: OrderStatus = OrderStatus.PENDING
    total_amount: float = Field(..., alias="totalAmount")

    class Settings:
        name = "orders"
