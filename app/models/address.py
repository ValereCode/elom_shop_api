from pydantic import BaseModel, Field
from typing import Optional

class Address(BaseModel):
    line1: str
    line2: Optional[str] = None
    city: str
    postal_code: str = Field(..., alias="postalCode")
    country: str
