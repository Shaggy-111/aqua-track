from pydantic import BaseModel, field_validator
from typing import Optional
from enum import Enum
from datetime import datetime

class OrderTypeEnum(str, Enum):
    customer = "customer"
    commercial = "commercial"

class OrderStatusEnum(str, Enum):
    pending = "pending"
    delivered = "delivered"

class OrderCreate(BaseModel):
    quantity: int
    address: str

class UpdateOrderStatus(BaseModel):
    order_id: int
    new_status: OrderStatusEnum

    @field_validator("new_status")
    def validate_status(cls, v):
        allowed_statuses = ["Delivered", "Cancelled", "In Transit"]
        if v not in allowed_statuses:
            raise ValueError(f"Status must be one of {allowed_statuses}")
        return v


class OrderOut(BaseModel):
    id: int
    user_id: int
    quantity: int
    address: str
    status: OrderStatusEnum
    type: OrderTypeEnum
    delivery_person_id: Optional[int]
    store_id: Optional[int]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
