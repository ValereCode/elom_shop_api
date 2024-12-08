from beanie import Document
from pydantic import Field
from bson import ObjectId
from datetime import datetime
from enum import Enum

class PaymentMethod(str, Enum):
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"

class Payment(Document):
    order_id: ObjectId = Field(..., alias="orderId")
    amount: float
    payment_date: datetime = Field(default_factory=datetime.now, alias="paymentDate")
    payment_method: PaymentMethod = Field(..., alias="paymentMethod")

    class Settings:
        name = "payments"
