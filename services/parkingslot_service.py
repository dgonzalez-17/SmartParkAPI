from models.parkingslot_model import Parkingslot
from config.database import MongoClientSingleton
from schemas.parkingslot_schema import parkingslotEntity, parkingslotsEntity

class ParkingslotService:
    def __init__(self):
        self.db = MongoClientSingleton().get_database()
    
    def get_all_slots(self):
        return parkingslotsEntity(self.db.parkingslot.find())
    
    def create_slot(self, slot: Parkingslot):
        new_slot = dict(slot)
        del new_slot['id']
        id = self.db.parkingslot.insert_one(new_slot).inserted_id
        slot = self.db.parkingslot.find_one({'_id': id})
        return parkingslotEntity(slot)
    
    def update_slot(self, slot_id:str, slot: Parkingslot):
        slot = dict(slot)
        del slot['id']
        self.db.parkingslot.find_one_and_update({'_id': slot_id}, {'$set': slot})
        return parkingslotEntity(self.db.parkingslot.find_one({'_id': slot_id}))
    
    def get_avalable_slots(self):
        return parkingslotsEntity(self.db.parkingslot.find({"busyStatus": False}))

    
