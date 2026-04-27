from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import supabase

router = APIRouter()

class Farm(BaseModel):
    name: str
    farmer_name: Optional[str] = None
    location: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    produce_type: Optional[str] = None

@router.get("/")
def get_farms():
    response = supabase.table("farms").select("*").execute()
    return response.data

@router.post("/")
def create_farm(farm: Farm):
    response = supabase.table("farms").insert(farm.model_dump()).execute()
    return response.data[0]

@router.get("/{farm_id}")
def get_farm(farm_id: str):
    response = supabase.table("farms").select("*").eq("id", farm_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Farm not found")
    return response.data[0]