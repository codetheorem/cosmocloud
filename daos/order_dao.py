from entities.order import Order, order_serializer
from daos.db import db
from bson.objectid import ObjectId



class OrderDAO:
    def __init__(self) -> None:
        pass

    def get_all_orders(self, limit: int, offset: int):
        data = list(db.orders.find({}, skip = ( offset - 1 ) * limit if offset > 0 else 0 , limit=limit))
        return [order_serializer(order) for order in data]
    
    def get_order(self, order_id: str):
        data = list(db.orders.find({"_id": ObjectId(order_id)}))
        return [order_serializer(order) for order in data]
    
    def add_one_order(self, order: Order):
        try:
            order = order.dict(exclude_none=True)
            order = db.orders.insert_one(order)
            return order
        except Exception as e:
            return e