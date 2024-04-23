# app/services/mi_servicio.py

from infrastructure.repository_impl_mongo import UserRepositoryMongo, PostRepositoryMongo

class MiServicioMongo:
    def __init__(self, user_repo: UserRepositoryMongo, post_repo: PostRepositoryMongo):
        self.user_repo = user_repo
        self.post_repo = post_repo

    def get_users(self):
        users = self.user_repo.get()
        return users

    def get_posts(self):
        post = self.post_repo.get()
        return post