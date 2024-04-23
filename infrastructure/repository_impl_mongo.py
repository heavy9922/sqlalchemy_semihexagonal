from app.repositories.base_repository_mongo import BaseRepositoryMongo

class UserRepositoryMongo(BaseRepositoryMongo):
    def get_collection_name(self):
        return "users"

    def get(self):
        return self.get_collection().find()
    
    def save(self, name: str, email: str):
        users_collection = self.get_collection()
        new_user = {
            "name": name,
            "email": email
        }
        users_collection.insert_one(new_user)

class PostRepositoryMongo(BaseRepositoryMongo):
    def get_collection_name(self):
        return "posts"

    def get(self):
        return self.get_collection().find()
    
    def save(self, title:str,  content: str, author: str):
        users_collection = self.get_collection()
        new_post = {
            "title": title,
            "content" : content,
            "author" : author,
        }
        users_collection.insert_one(new_post)