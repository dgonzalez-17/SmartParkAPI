import datetime
from config.database import MongoClientSingleton
from models.earning_model import Earning
from schemas.earning_schema import earningEntity, earningsEntity
import re


class EarningService:
    def __init__(self):
        self.db = MongoClientSingleton().get_database()
    
    def get_all_earnings(self):
        return earningsEntity(self.db.earning.find())
    
    def get_one_earning(self, id):
        return earningEntity(self.db.earning.find_one({'_id': id}))
    
    def create_one_earning(self, earning: Earning):
        new_earning = dict(earning)
        del new_earning['id']
        id =  self.db.earning.insert_one(new_earning).inserted_id
        return earningEntity(self.db.earning.find_one({'_id': id}))
    
    def update_one_earning(self, id: str, earning: Earning):
        earning = dict(earning)
        del earning['id']
        self.db.earning.find_one_and_update({'_id': id},{'$set': earning})
        return earningEntity(self.db.earning.find_one({'_id': id}))
    
    def update_one_earning_by_day(self, earning: Earning):
        earning = dict(earning)
        del earning['id']
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        earning_db = self.db.earning.find_one({'date':today})
        if not earning_db:
            id = self.db.earning.insert_one(earning).inserted_id
            earning_db = self.db.earning.find_one({'_id': id})
            return earningEntity(earning_db)
        earning_db['earnings'] += earning['earnings']
        count = self.db.earning.update_one({'_id': earning_db['_id']}, {'$set': earning_db}).modified_count
        if count > 0:
            return earningEntity(self.db.earning.find_one({'_id': earning_db['_id']}))
        else: 
            return {"error": "Earning is not updated"}
    
    def get_today_earnings(self):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        earning = self.db.earning.find_one({'date':today})
        if not earning:
            return None
        earning = dict(earning)
        return earning['earnings']
    
    def get_month_earnings(self):
        year_and_month =  datetime.datetime.now().strftime("%Y-%m")
        regex = re.compile(r'^'+re.escape(year_and_month)+ r'-\d{2}$')
        earnings = self.db.earning.find({"date":{"$regex": regex}})
        try:
            earnings_dict = earningsEntity(earnings)
            total = sum(earn_dict['earnings'] for earn_dict in earnings_dict)
            print(total)
            return total
        except Exception as e:
            print(e)
            return None