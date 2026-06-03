from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import List

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: int
    quantity: int


    @field_validator("id")
    def validate_id(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("ID must be greater than 0")
        return v
    
    @field_validator("name")
    def validate(cls, v: str) -> str:
        if len(v) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return v.strip()
    
    @field_validator("price")
    def validate_price(cls, v:int) -> int:
        if v <= 0:
            raise ValueError("Price must be greater than 0")
        return v
    
    @field_validator("quantity")
    def validate_quantity(cls, v: int) -> int:
        if v < 0:
            raise ValueError("Quantity cannot be negative")
        return v
    