from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity_in_stock: int

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class Item(ItemBase):
    id: UUID

    class Config:
        orm_mode: True
