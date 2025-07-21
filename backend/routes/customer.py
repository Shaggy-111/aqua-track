from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from models.order import Order
from schemas.order import OrderCreate, OrderOut
from utils.auth import get_current_user
from models.user import User

router = APIRouter()

@router.post("/order", response_model=OrderOut)
def place_order(order: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if order.quantity < 1:
        raise HTTPException(status_code=400, detail="Order quantity must be at least 1")

    new_order = Order(
        user_id=current_user.id,
        quantity=order.quantity,
        address=order.address,
        status="pending",
        type="customer"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@router.get("/test-customer")
def test_customer():
    return {"msg": "Customer route working"}


