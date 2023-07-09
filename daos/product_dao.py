from entities.product import Product, product_serializer
from daos.db import db
from bson.objectid import ObjectId



class ProductDAO:
    def __init__(self) -> None:
        pass

    def get_all_products(self):
        data = list(db.products.find({}))
        return [product_serializer(product) for product in data]
    
    def update_one_product(self, product_id: str, product: Product):
        try:
            product  = db.products.update_one({"_id": ObjectId(product_id)}, {"$set": product.dict(exclude_none=True)})
            return product
        except Exception as e:
            return e