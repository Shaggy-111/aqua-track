from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from models.order import Order
from schemas.order import OrderOut
from typing import List
from models.user import User,RoleEnum 
from schemas.order import UpdateOrderStatus
from models import order as order_model


router = APIRouter()

@router.get("/all-orders", response_model=List[OrderOut])
def get_all_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    return orders

@router.get("/admin-health")
def health_check():
    return {"status": "admin OK"}

@router.get("/admin/view_all_customers")
def view_all_customers(db: Session = Depends(get_db)):
    customers = db.query(User).filter(User.role == RoleEnum.customer).all()
    return {
        "status": "success",
        "results": len(customers),
        "data": [customer.to_dict() for customer in customers]
    }


@router.get("/view_all_customers")
def view_pending_customers(db: Session = Depends(get_db)):
    pending_customers = db.query(User).filter(User.status == "pending").all()
    return {
        "status": "success",
        "results": len(pending_customers),
        "data": [customer.to_dict() for customer in pending_customers]
    }
@router.put("/admin/assign_order")
def assign_order(order_id: int, delivery_person_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if order.delivery_person_id == delivery_person_id:
        raise HTTPException(status_code=400, detail="Order already assigned to this delivery person")

    if order.delivery_person_id:
        raise HTTPException(status_code=400, detail="Order already assigned to a delivery person")

    delivery_person = db.query(User).filter(User.id == delivery_person_id, User.role == "delivery").first()
    if not delivery_person:
        raise HTTPException(status_code=404, detail="Delivery person not found")

    order.delivery_person_id = delivery_person_id
    db.commit()

    return {"message": "Delivery person assigned successfully"}


@router.put("/admin/update_status")
def update_status(order_id: int, status: str, db: Session = Depends(get_db)):
    try:
        order = db.query(Order).filter(Order.id == order_id).first()
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")

        order.status = status
        db.commit()

        return {
            "status": "success",
            "message": "Order status updated successfully",
            "order_id": order.id,
            "new_status": order.status
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/update_status")
def update_order_status(data: UpdateOrderStatus, db: Session = Depends(get_db)):
    order = db.query(order_model.Order).filter(order_model.Order.id == data.order_id).first()
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = data.new_status
    db.commit()
    db.refresh(order)

    return {"msg": "Order status updated", "order_id": order.id, "new_status": order.status}