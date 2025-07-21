from pydantic import BaseModel
from typing import Optional
from enum import Enum

class OrderTypeEnum(str, Enum):
    customer = "customer"
    commercial = "commercial"

class OrderStatusEnum(str, Enum):
    pending = "pending"
    delivered = "delivered"

class OrderCreate(BaseModel):
    quantity: int
    address: str

class OrderOut(BaseModel):
    id: int
    user_id: int
    quantity: int
    address: str
    status: OrderStatusEnum
    type: OrderTypeEnum

    class Config:
        orm_mode = True
