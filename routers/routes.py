from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import supabase

router = APIRouter()

class Route(BaseModel):
    shipment_id: str
    waypoints: Optional[List[dict]] = []
    distance_km: Optional[float] = None
    estimated_duration_hrs: Optional[float] = None
    status: Optional[str] = "active"

@router.get("/")
def get_routes():
    response = supabase.table("routes").select("*, shipments(cargo_type, destination, status)").execute()
    return response.data

@router.post("/")
def create_route(route: Route):
    response = supabase.table("routes").insert(route.model_dump()).execute()
    return response.data[0]

@router.get("/{route_id}")
def get_route(route_id: str):
    response = supabase.table("routes").select("*").eq("id", route_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Route not found")
    return response.data[0]