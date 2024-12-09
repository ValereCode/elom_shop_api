from beanie import Document
from pydantic import Field
from datetime import datetime
from enum import Enum
from beanie import Link
from .order import Order


class PaymentMethod(str, Enum):
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"

class Payment(Document):
    order: Link[Order]
    amount: float
    payment_date: datetime = Field(default_factory=datetime.now, alias="paymentDate")
    payment_method: PaymentMethod = Field(..., alias="paymentMethod")

    class Settings:
        name = "payments"
