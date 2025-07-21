from pydantic import BaseModel, EmailStr
from pydantic import BaseModel

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    role: str  # "customer", "vendor", "admin"

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    role: str

class Config:
        from_attributes = True
    
class Token(BaseModel):
    access_token: str
    token_type: str

class UserLogin(BaseModel):
    email: str
    password: str





