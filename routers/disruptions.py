from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from database import supabase

router = APIRouter()

class Disruption(BaseModel):
    route_id: str
    type: str          # weather, road, spoilage
    severity: str      # low, medium, high
    description: Optional[str] = None

@router.get("/")
def get_disruptions():
    response = supabase.table("disruptions").select("*").is_("resolved_at", "null").execute()
    return response.data

@router.post("/")
def report_disruption(disruption: Disruption):
    response = supabase.table("disruptions").insert(disruption.model_dump()).execute()
    return response.data[0]
