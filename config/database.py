from motor.motor_asyncio import AsyncIOMotorClient

class MongoClientSingleton:
    uri = "mongodb+srv://root:root@smartpark.3gvpliy.mongodb.net/?retryWrites=true&w=majority"
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls.client = AsyncIOMotorClient(cls.uri)
        return cls._instance

    def get_database(self):
        try:
            db = self.client['smartpark_db']
            return db
        except Exception as e:
            print("Connection failed: ", e)
            exit(0)
