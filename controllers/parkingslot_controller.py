from fastapi import APIRouter, status, Response
from models.parkingslot_model import Parkingslot
from schemas.parkingslot_schema import parkingslotEntity, parkingslotsEntity
from services.parkingslot_service import ParkingslotService

parkingslot_router = APIRouter(prefix="/parkingslot")
parkingslot_service = ParkingslotService()

@parkingslot_router.post("/", tags=["Parkingslot"])
def create_slot(data: Parkingslot):
    return parkingslot_service.create_slot(data)

@parkingslot_router.get("/", tags=["Parkingslot"])
def get_all_slots():
    return parkingslot_service.get_all_slots()