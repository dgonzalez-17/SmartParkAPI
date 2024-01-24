from fastapi import APIRouter
from models.price_model import Price
from services.price_service import PriceService

price_router = APIRouter(prefix="/price")
price_service = PriceService()


@price_router.get("/", tags=["Price"])
def get_all():
    return price_service.get_all_prices()


@price_router.post("/", tags=["Price"])
def create_one(price: Price):
    return price_service.create_price(price)


@price_router.get("/{id}", tags=["Price"])
def get_one(id: str, price: Price):
    return price_service.update_price(id, price)


@price_router.put("/{name}", tags=["Price"])
def get_one_by_name(name: str, price: Price):
    return price_service.update_price_by_name(name, price)
