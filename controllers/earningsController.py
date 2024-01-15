from fastapi import APIRouter, HTTPException
from models.earningsModels import Earnings
from repositories.earningsRepository import EarningsRepository

earningsRouter = APIRouter(prefix="/earnings")

earningsRepo = EarningsRepository()

@earningsRouter.get("/getAll")
async def get():
    return await earningsRepo.getAllEarnings()

@earningsRouter.post("/new")
async def create(earning: Earnings):
    return await earningsRepo.createEarning(earning)
