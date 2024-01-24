from fastapi import APIRouter, status, Response
from models.historical_model import Historical
from schemas.historical_schema import historicalEntity, historicalsEntity
from services.historical_service import HistoricalService

historical_router = APIRouter(prefix='/historical')
historical_service = HistoricalService()

@historical_router.get('/', response_model=list[Historical], tags=['Historical'])
def get_all():
    return historical_service.get_all_historicals()

@historical_router.post('/', response_model=Historical, tags=['Historical'])
def create_one(historical: Historical):
    return historical_service.create_historical(historical)

@historical_router.get('/{id}', response_model=Historical, tags=['Historical'])
def get_one(id: str):
    return historical_service.get_one_historical(id)

@historical_router.put('/{id}', response_model=Historical, tags=['Historical'])
def update_one(id: str, historical: Historical):
    return historical_service.update_one_historical(id, historical)

@historical_router.put('/paid/', tags=['Historical'])
def update_paid_one(historical: Historical):
    return historical_service.update_one_paid_by_plate(historical)