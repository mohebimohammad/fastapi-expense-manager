from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import List, Optional

class Item(BaseModel):
    title: str
    description: str
    price: float
    
    @field_validator("title")
    def validate(cls, v: str) -> str:
        if len(v) < 2:
            raise ValueError("title must be at least 2 characters long")
        return v.strip()
    
    @field_validator("description")
    def validate_quantity(cls, v: str) -> str:
        if len(v) < 10:
            raise ValueError("description must be at least 10 characters long")
        return v.strip()

    @field_validator("price")
    def validate_price(cls, v:float) -> float:
        if v <= 0:
            raise ValueError("Price must be greater than 0")
        return v
    


class ItemResponse(Item):
    id: int
    timestap: Optional[datetime] = None

