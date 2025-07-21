from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from database.db import get_db
from models.user import User
from utils.auth import verify_password, hash_password
from utils.jwt import create_access_token
from schemas.user import UserCreate, UserOut

router = APIRouter()

# -------- LOGIN --------
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        print("✅ Login request received:", form_data.username)

        user = db.query(User).filter(User.email == form_data.username).first()
        if not user or not verify_password(form_data.password, user.password):
            print("❌ Invalid login attempt")
            raise HTTPException(status_code=400, detail="Invalid email or password")

        access_token = create_access_token(data={"sub": user.email})
        print("✅ Login successful")

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "email": user.email,
            "full_name": user.full_name,
            "role": user.role
        }

    except Exception as e:
        print("🔥 Exception during login:", str(e))
        raise HTTPException(status_code=500, detail="Internal server error")

# -------- SIGNUP --------
@router.post("/signup", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user.password)

    print("⚠️ User class is coming from:", User.__module__)
    print("⚠️ User class type:", type(User))

    print("DEBUG ➤ User class from:", User.__module__)
    print("DEBUG ➤ User fields:", User.__table__.columns.keys())


    new_user = User(
        email=user.email,
        password=hashed_pw,
        full_name=user.full_name,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


