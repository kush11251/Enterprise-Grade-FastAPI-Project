from models import User
from database import db

class UserRepository:
    def get_users(self):
        return db.query(User).all()

user_repository = UserRepository()