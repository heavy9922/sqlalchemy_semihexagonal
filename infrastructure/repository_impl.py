from app.repositories.base_repository import UserRepository
from app.domain.models import User
from data.database import get_session

class SQLAlchemyUserRepository(UserRepository):
    def add_user(self, user: User):
        session = get_session()
        session.add(user)
        session.commit()
        session.close()

    def get_all_users(self):
        session = get_session()
        users = session.query(User).all()
        session.close()
        return users
