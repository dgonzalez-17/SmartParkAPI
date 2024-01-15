from typing import Generic, TypeVar, get_args
from config.database import MongoClientSingleton
T = TypeVar("T")


class BaseRepository(Generic[T]):
    _db = MongoClientSingleton().get_database() 

    def __init__(self):
        theClass = get_args(self.__orig_bases__[0])
        self.collection = theClass[0].__name__.lower()
        self.db = self._db
