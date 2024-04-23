from sqlalchemy import Column, Integer, String
from data.database import Base
from data.database import get_engine

class User(Base):
    __tablename__ = 'users_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    def __repr__(self):
        return f"<User(name='{self.name}')>"
