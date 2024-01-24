from fastapi import FastAPI
from controllers.price_controller import price_router
from controllers.telebot_controller import telegram_router
from controllers.parkingslot_controller import parkingslot_router
from controllers.historical_controller import historical_router
from controllers.earning_controller import earning_router

app = FastAPI()

app.include_router(telegram_router)
app.include_router(price_router)
app.include_router(parkingslot_router)
app.include_router(historical_router)
app.include_router(earning_router)
