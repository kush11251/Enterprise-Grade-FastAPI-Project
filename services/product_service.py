from models import Product
from repository import product_repository

class ProductService:
    def get_products(self):
        return product_repository.get_products()

product_service = ProductService()