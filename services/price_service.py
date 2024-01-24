from models.price_model import Price
from config.database import MongoClientSingleton
from schemas.price_schema import priceEntity, pricesEntity

class PriceService:
    def __init__(self):
        self.db = MongoClientSingleton().get_database()

    def get_all_prices(self):
        return pricesEntity(self.db.price.find())
    
    def get_one_price_by_name(self, name:str):
        price = dict(self.db.price.find_one({'typeVehicle': name}))
        return price['price']


    def create_price(self, price: Price):
        new_price = dict(price)
        del new_price['id']
        id = self.db.price.insert_one(new_price).inserted_id
        price = self.db.price.find_one({"_id": id})
        return priceEntity(price)
    
    def update_price(self, price_id: str, price: Price):
        price = dict(price)
        del price['id']
        self.db.price.find_one_and_update({"_id": price_id}, {"$set": price})
        return priceEntity(self.db.price.find_one({"_id": price_id}))
    
    def update_price_by_name(self, name: str, price: Price):
        price = dict(price)
        del price['id']
        self.db.price.find_one_and_update({"typeVehicle": name}, {"$set": price})
        return priceEntity(self.db.price.find_one({"typeVehicle": name}))
    
    def update_price_value_by_name(self, name: str, price: Price):
        price_db = priceEntity(self.db.price.find_one({"typeVehicle": name}))
        price = dict(price)
        del price['id']
        if price['description'] == None:
            price['description'] = price_db['description']
        self.db.price.find_one_and_update({"typeVehicle": name}, {"$set": price})
        return priceEntity(self.db.price.find_one({"typeVehicle": name}))
    
