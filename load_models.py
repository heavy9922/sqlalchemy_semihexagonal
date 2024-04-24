from data.database import Base
from data.database import get_engine

from app.domain.models_sql import User
def load_models():
    engine = get_engine()
    Base.metadata.create_all(bind=engine)
    return "models created successfully"

if __name__ == '__main__':
    load_models()