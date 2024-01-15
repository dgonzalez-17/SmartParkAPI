from fastapi import APIRouter, HTTPException
from models.pricesModel import Prices
from repositories.pricesRepository import PricesRepository

pricesRouter = APIRouter(prefix="/prices")

pricesRepo = PricesRepository()

@pricesRouter.get("/getAll")
async def get():
    return await pricesRepo.getAllPrices()

@pricesRouter.post("/new")
async def create(price: Prices):
    return await pricesRepo.createPrice(price)
