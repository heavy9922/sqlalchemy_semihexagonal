from abc import ABC, abstractmethod
from app.domain.models import User

class UserRepository(ABC):
    @abstractmethod
    def add_user(self, user: User):
        pass

    @abstractmethod
    def get_all_users(self):
        pass
