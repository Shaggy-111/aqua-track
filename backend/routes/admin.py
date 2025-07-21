from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from models.order import Order
from schemas.order import OrderOut
from typing import List

router = APIRouter()

@router.get("/all-orders", response_model=List[OrderOut])
def get_all_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    return orders

@router.get("/admin-health")
def health_check():
    return {"status": "admin OK"}