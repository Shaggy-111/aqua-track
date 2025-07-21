from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import (
    user,
    admin,
    delivery_routes,
    customer,
    commercial,
    login,
    region,
)
from backend.database.db import Base, engine
from backend import models

# Create DB tables (optional to move to setup_db.py)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AquaTrack API")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include route handlers
app.include_router(user.router, tags=["User"])
app.include_router(admin.router, tags=["Admin"])
app.include_router(delivery_routes.router, tags=["Delivery"])
app.include_router(customer.router, tags=["Customer"])
app.include_router(commercial.router, tags=["Commercial"])
app.include_router(login.router, tags=["Auth/Login"])
app.include_router(region.router, tags=["Region"], prefix="/region")

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to AquaTrack Backend API!"}
