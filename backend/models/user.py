from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base
from enum import Enum as PyEnum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database.db import Base

# 🟡 Define Enum for roles
class RoleEnum(PyEnum):
    superadmin = "superadmin"
    admin = "admin"
    vendor = "vendor"
    delivery = "delivery"
    customer = "customer"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)

    role = Column(Enum(RoleEnum), nullable=False)
    region_id = Column(Integer, ForeignKey("regions.id"), nullable=True)
    status = Column(String, default="pending")

    region = relationship("Region", backref="users")
    orders = relationship("Order", back_populates="user", foreign_keys="Order.user_id")

    # ✅ Add this method inside the User class
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "full_name": self.full_name,
            "role": self.role.value if self.role else None,
            "status": self.status,
            "region_id": self.region_id
        }



    

