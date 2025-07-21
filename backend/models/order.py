from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database.db import Base
import enum

class OrderTypeEnum(str, enum.Enum):
    customer = "customer"
    commercial = "commercial"

class OrderStatusEnum(str, enum.Enum):
    pending = "pending"
    delivered = "delivered"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    quantity = Column(Integer)
    address = Column(String)
    status = Column(Enum(OrderStatusEnum), default=OrderStatusEnum.pending)
    type = Column(Enum(OrderTypeEnum), default=OrderTypeEnum.customer)

    user = relationship("User", back_populates="orders")

    def __repr__(self):
        return f"<Order(id={self.id}, user_id={self.user_id}, quantity={self.quantity}, status={self.status}, type={self.type})>"
