from app.repositories.base_repository import UserRepository
from app.domain.models_sql import User

class MiServicio:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def agregar_usuario(self, nombre):
        user = User(name=nombre)
        self.user_repo.add_user(user)

    def obtener_usuarios(self):
        return self.user_repo.get_all_users()
