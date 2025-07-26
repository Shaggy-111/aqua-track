from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from models.region import Region
from schemas.region import RegionCreate, RegionOut

router = APIRouter()

# ----- Create a new region -----
@router.post("/", response_model=RegionOut)
def create_region(region: RegionCreate, db: Session = Depends(get_db)):
    existing_region = db.query(Region).filter(Region.name == region.name).first()
    if existing_region:
        raise HTTPException(status_code=400, detail="Region already exists")
    new_region = Region(name=region.name)
    db.add(new_region)
    db.commit()
    db.refresh(new_region)
    return new_region

# ----- Get all regions -----
@router.get("/", response_model=list[RegionOut])
def get_regions(db: Session = Depends(get_db)):
    return db.query(Region).all()
