from models import Product
from database import db

class ProductRepository:
    def get_products(self):
        return db.query(Product).all()

product_repository = ProductRepository()