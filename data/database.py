from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def get_engine():
    return create_engine("postgresql://admin:admin1234@localhost:5436/integrations?client_encoding=utf8", echo=True)

def get_session():
    engine = get_engine()
    session = sessionmaker(bind=engine)
    return session()
