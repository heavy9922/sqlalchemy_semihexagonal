from injector import inject, Injector, Module
from app.services.mi_servicio import MiServicio
from infrastructure.repository_impl import SQLAlchemyUserRepository
from app.repositories.base_repository import UserRepository

class AppModule(Module):
    def configure(self, binder):
        binder.bind(UserRepository, to=SQLAlchemyUserRepository)

def main():
    injector = Injector([AppModule()])
    user_repo = injector.get(UserRepository)
    mi_servicio = MiServicio(user_repo)

    mi_servicio.agregar_usuario("Alice")
    mi_servicio.agregar_usuario("Bob")

    usuarios = mi_servicio.obtener_usuarios()
    print("Usuarios en la base de datos:")
    for usuario in usuarios:
        print(usuario)

if __name__ == "__main__":
    main()
