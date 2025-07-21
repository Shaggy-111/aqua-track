from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

# 🟡 Avoid circular imports at runtime
# Don't import Region or Order unless absolutely needed in this file

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    role = Column(String, nullable=False)  # superadmin, admin, vendor, etc.

    region_id = Column(Integer, ForeignKey("regions.id"), nullable=True)

    region = relationship("Region", backref="users")
    orders = relationship("Order", back_populates="user")  # if you have models.order


    

