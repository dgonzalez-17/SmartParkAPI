import datetime

from fastapi import Response
import pymongo
from models.historical_model import Historical
from config.database import MongoClientSingleton
from schemas.historical_schema import historicalEntity, historicalsEntity
from utils.historical_helper import get_total_value, update_earning

class HistoricalService:
    def __init__(self):
        self.db = MongoClientSingleton().get_database()
    
    def get_all_historicals(self):
        return historicalsEntity(self.db.historical.find())
    
    def get_one_historical(self, id: str):
        return historicalEntity(self.db.historical.find_one({'_id': id}))
    
    def create_historical(self, historical: Historical):
        new_historical = dict(historical)
        del new_historical['id']
        print(new_historical)
        id = self.db.historical.insert_one(new_historical).inserted_id
        historical = self.db.historical.find_one({'_id': id})
        return historicalEntity(historical)
    
    def update_one_historical(self, id: str, historical: Historical):
        historical = dict(historical)
        del historical[id]
        self.db.historical.find_one_and_update({'_id': id},{'$set': historical})
        return historicalEntity(self.db.historical.find_one({'_id': id}))
    
    def update_one_paid_by_plate(self, historical: Historical):
        historical = dict(historical)
        historical_db = self.db.historical.find_one({'plate': historical['plate'], 'itsPaid': False})
        if not historical_db:
            return Response(status_code=304)
        else:
            historical_db = dict(historical_db)
        del historical_db['_id']
        historical_db['checkOutTime'] = datetime.datetime.now()
        historical_db['totalValue'] = get_total_value(historical_db)
        historical_db['itsPaid'] = True
        count = self.db.historical.update_one({'plate':historical['plate'], 'itsPaid': False},{'$set': historical_db}).modified_count
        if count > 0 and update_earning(historical_db['totalValue']):
            historical_final =  historicalsEntity(self.db.historical.find({'plate': historical['plate']}).sort('checkOutTime', pymongo.DESCENDING))
            return historical_final[0]                                    
        else: 
            return Response(status_code=304)


