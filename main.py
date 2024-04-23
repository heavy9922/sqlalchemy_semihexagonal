from injector import Injector, Module, Binder
from app.services.mi_servicio import MiServicio
from app.services.mi_servicio_mongo import MiServicioMongo
from infrastructure.repository_impl import SQLAlchemyUserRepository
from app.repositories.base_repository import UserRepository
from data.mongo import DatabaseMongo
from infrastructure.repository_impl_mongo import PostRepositoryMongo, UserRepositoryMongo

class AppModule(Module):
    def configure(self, binder: Binder):
        binder.bind(UserRepository, to=SQLAlchemyUserRepository)

class AppModuleMongo(Module):
    def configure(self, binder: Binder):
        db_url = "mongodb://admin:password@localhost:27019/?authSource=integrations&tls=false&ssl=false"
        db_name = "integrations"
        database = DatabaseMongo(db_url, db_name)
        
        binder.bind(UserRepositoryMongo, to=UserRepositoryMongo(database))
        binder.bind(PostRepositoryMongo, to=PostRepositoryMongo(database))

def main():
    # Configuración para SQL
    injector_sql = Injector([AppModule()])
    user_repo_sql = injector_sql.get(UserRepository)
    mi_servicio_sql = MiServicio(user_repo_sql)

    mi_servicio_sql.agregar_usuario("Alice")
    mi_servicio_sql.agregar_usuario("Bob")

    usuarios_sql = mi_servicio_sql.obtener_usuarios()
    print("Usuarios en la base de datos SQL:")
    for usuario in usuarios_sql:
        print(usuario)

    injector_mongo = Injector([AppModuleMongo()])
    # Crear usuarios en MongoDB
    user_repo_mongo = injector_mongo.get(UserRepositoryMongo)
    post_repo_mongo = injector_mongo.get(PostRepositoryMongo)
    user_repo_mongo.save("Alice", "alice@example.com")
    user_repo_mongo.save("Bob", "bob@example.com")
    post_repo_mongo.save('test 1','lorem ipsum dolor sit amet, consectetur adip', 'yo')

    # Obtener y mostrar usuarios en MongoDB
    mi_servicio_mongo = MiServicioMongo(user_repo_mongo, post_repo_mongo)
    
    usuarios_mongo = mi_servicio_mongo.get_users()
    post_mongo = mi_servicio_mongo.get_posts()
    print("Usuarios en la base de datos MongoDB:")
    for usuario in post_mongo:
        print(usuario)
    for post in usuarios_mongo:
        print(post)


if __name__ == "__main__":
    main()
