import json
from typing import Union
from fastapi import FastAPI, Body
from pymongo import MongoClient
from entities.product import Product, product_serializer
from entities.order import Order, order_serializer
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from typing import Annotated
from daos.product_dao import ProductDAO
from daos.order_dao import OrderDAO

app = FastAPI()


@app.get("/products/")
def get_all_products():
    products = ProductDAO().get_all_products()
    return products

@app.put("/products/{product_id}")
def update_product(product_id: str, product: Product):
    try:
        product = ProductDAO().update_one_product(product_id, product)
        return {"status": "success", "product": product}
    except:
        return {"status": "Failed"}

@app.post("/orders/")
def add_order(order: Order):
    try:
        order = OrderDAO().add_one_order(order)
        return {"status": "success", "order": order}
    except:
        return {"status": "Failed"}

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    order = OrderDAO().get_order(order_id)
    return order

@app.get("/orders/")
def get_all_orders(limit: int, offset: int):
    orders = OrderDAO().get_all_orders(limit, offset)
    return orders


