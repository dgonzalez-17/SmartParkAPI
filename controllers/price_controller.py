from fastapi import APIRouter, status, Response
from models.price_model import Price
from schemas.price_schema import priceEntity, pricesEntity
from services.price_service import PriceService

price_router = APIRouter(prefix="/price")
price_service = PriceService()


@price_router.get("/", response_model=list[Price], tags=["Price"])
def get_all():
    return price_service.get_all_prices()


@price_router.post("/", response_model=Price, tags=["Price"])
def create_one(price: Price):
    return price_service.create_price(price)


@price_router.get("/{id}", response_model=list[Price], tags=["Price"])
def get_one(id: str, price: Price):
    return price_service.update_price(id, price)


@price_router.put("/{name}", response_model=Price, tags=["Price"])
def get_one_by_name(name: str, price: Price):
    return price_service.update_price_by_name(name, price)
