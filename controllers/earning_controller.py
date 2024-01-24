from fastapi import APIRouter, status, Response
from models.earning_model import Earning
from schemas.earning_schema import earningEntity, earningsEntity
from services.earning_service import EarningService

earning_router = APIRouter(prefix='/earning')
earning_service = EarningService()

@earning_router.get('/', response_model=list[Earning], tags=['Earning'])
def get_all():
    return earning_service.get_all_earnings()

@earning_router.get('/{id}', response_model=Earning, tags=['Earning'])
def get_one(id: str):
    return earning_service.get_one_earning(id)

@earning_router.post('/', response_model=Earning, tags=['Earning'])
def create_one(earning: Earning):
    return earning_service.create_one_earning(earning)

@earning_router.put('/{id}', response_model=Earning)
def update_one(id: str, earning: Earning):
    return earning_service.get_one_earning(id, earning)
