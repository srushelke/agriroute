from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import supabase

router = APIRouter()

class Shipment(BaseModel):
    farm_id: str
    destination: str
    dest_latitude: Optional[float] = None
    dest_longitude: Optional[float] = None
    cargo_type: str
    quantity_kg: float
    departure_time: Optional[str] = None
    estimated_arrival: Optional[str] = None
    status: Optional[str] = "pending"

@router.get("/")
def get_shipments():
    response = supabase.table("shipments").select("*, farms(name, location)").execute()
    return response.data

@router.post("/")
def create_shipment(shipment: Shipment):
    response = supabase.table("shipments").insert(shipment.model_dump()).execute()
    return response.data[0]

@router.patch("/{shipment_id}/status")
def update_status(shipment_id: str, status: str):
    response = supabase.table("shipments").update({"status": status}).eq("id", shipment_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return response.data[0]