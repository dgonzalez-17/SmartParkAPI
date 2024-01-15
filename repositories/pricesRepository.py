from models.pricesModel import Prices
from repositories.baseRepository import BaseRepository


class PricesRepository(BaseRepository[Prices]):
    def __init__(self):
        super().__init__()
    
    async def getAllPrices(self):
        collection = self.db[self.collection]
        prices = await collection.find().to_list(100)
        return [Prices(**data) for data in prices]
    
    async def createPrice(self, price: Prices):
        collection = self.db[self.collection]
        result = await collection.insert_one(price.model_dump())
        return {"id": str(result.inserted_id)}