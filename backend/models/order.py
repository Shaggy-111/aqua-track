from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database.db import Base
import enum
from sqlalchemy import Column, DateTime
from datetime import datetime, timezone


class OrderTypeEnum(str, enum.Enum):
    customer = "customer"
    commercial = "commercial"

class OrderStatusEnum(str, enum.Enum):
    pending = "pending"
    in_transit = "in_transit"
    delivered = "delivered"
    cancelled = "cancelled"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    quantity = Column(Integer)
    address = Column(String)
    status = Column(Enum(OrderStatusEnum), default=OrderStatusEnum.pending)
    type = Column(Enum(OrderTypeEnum), default=OrderTypeEnum.customer)
    delivery_person_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=True)  # ✅ Optional but useful
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # ✅ New
    
    
    #Relationships 
    user = relationship("User", back_populates="orders", foreign_keys=[user_id])
    delivery_person = relationship("User", foreign_keys=[delivery_person_id])
    store = relationship("Store", back_populates="orders")
    


    def __repr__(self):
        return f"<Order(id={self.id}, user_id={self.user_id}, quantity={self.quantity}, status={self.status}, type={self.type})>"
