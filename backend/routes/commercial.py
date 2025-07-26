from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from models.order import Order
from schemas.order import OrderCreate, OrderOut
from utils.auth import get_current_user
from models.user import User

router = APIRouter()

@router.post("/bulk-order", response_model=OrderOut)
def place_bulk_order(order: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if order.quantity < 50:
        raise HTTPException(status_code=400, detail="Bulk orders must be at least 50 units")

    new_order = Order(
        user_id=current_user.id,
        quantity=order.quantity,
        address=order.address,
        status="pending",
        type="commercial"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@router.get("/test-commercial")
def test_commercial():
    return {"msg": "Commercial route working"}

