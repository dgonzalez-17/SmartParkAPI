from fastapi import FastAPI
from controllers.pricesController import pricesRouter
from controllers.earningsController import earningsRouter

app = FastAPI()

app.include_router(pricesRouter)
app.include_router(earningsRouter)