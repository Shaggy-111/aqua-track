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


@router.get("/delivery/dashboard")
def delivery_dashboard(delivery_person_id: int, db: Session = Depends(get_db)):
    orders = db.query(Order).filter(Order.delivery_person_id == delivery_person_id).all()

    return {
        "status": "success",
        "total_orders": len(orders),
        "orders": [
            {
                "order_id": order.id,
                "status": order.status,
                "customer_id": order.customer_id,
                "delivery_address": order.delivery_address
            }
            for order in orders
        ]
    }



