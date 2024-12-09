from beanie import Document
from typing import Optional, List
from pydantic import EmailStr, Field
from .address import Address

class User(Document):
    name: str
    email: EmailStr
    password: str  # Ensure to hash passwords in practice
    addresses: Optional[List[Address]] = []
    phone_number: Optional[str] = Field(None, alias="phoneNumber")

    class Settings:
        name = "users"
