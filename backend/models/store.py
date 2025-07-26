# store.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=True)

    # 🔁 Relationship with orders
    orders = relationship("Order", back_populates="store")

    def __repr__(self):
        return f"<Store(id={self.id}, name={self.name})>"
