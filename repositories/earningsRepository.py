from models.earningsModels import Earnings
from repositories.baseRepository import BaseRepository


class EarningsRepository(BaseRepository[Earnings]):
    def __init__(self):
        super().__init__()
        
    async def getAllEarnings(self):
        collection = self.db[self.collection]
        prices = await collection.find().to_list(100)
        return [Earnings(**data) for data in prices]
    
    async def createEarning(self, earning: Earnings):
        collection = self.db[self.collection]
        result = await collection.insert_one(earning.model_dump())
        return {"id": str(result.inserted_id)}