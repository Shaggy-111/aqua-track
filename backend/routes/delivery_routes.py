from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from models.order import Order
from utils.auth import get_current_user
from models.user import User

print("✅ delivery.py loaded")


router = APIRouter()

@router.put("/deliver-order/{order_id}")
def deliver_order(order_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = "delivered"
    db.commit()
    return {"message": "Order marked as delivered"}


router.get("/test-delivery")
def test():
    return {"msg": "delivery test working"}

