from abc import ABC, abstractmethod
from typing import Any

class BaseRepositoryMongo(ABC):
    def __init__(self, database):
        self.database = database

    @abstractmethod
    def get_collection_name(self):
        pass

    def get_collection(self):
        return self.database.get_collection(self.get_collection_name())
    
    @abstractmethod
    def save(self, data: Any):
        pass

    @abstractmethod
    def get(self):
        pass