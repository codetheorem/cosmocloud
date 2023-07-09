import json
from typing import Union
from fastapi import FastAPI, Body
from pymongo import MongoClient
from entities.product import Product, product_serializer
from entities.order import Order, order_serializer
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from typing import Annotated



app = FastAPI()

client = MongoClient('mongodb+srv://hrishikeshagarwalv:Harsh2000@cluster0.c0onhzq.mongodb.net/?retryWrites=true&w=majority')

db = client.ecommerce_db


@app.get("/products/")
def get_all_products():
    data = list(db.products.find({}))
    return [product_serializer(product) for product in data]

@app.put("/products/{product_id}")
def update_product(product_id: str, product: Product):
    product  = db.products.update_one({"_id": ObjectId(product_id)}, {"$set": product.dict(exclude_none=True)})
    return product

@app.post("/orders/")
def add_order(order: Order):
    try:
        order = order.dict(exclude_none=True)
        order = db.orders.insert_one(order)
        return {"status": "success", "order": order}
    except:
        return {"status": "Failed"}

@app.get("/orders/{order_id}")
def get_orders(order_id: str):
    data = list(db.orders.find({"_id": ObjectId(order_id)}))
    return [order_serializer(order) for order in data]

@app.get("/orders/")
def get_orders(limit: int, offset: int):
    data = list(db.orders.find({}, skip = ( offset - 1 ) * limit if offset > 0 else 0 , limit=limit))
    return [order_serializer(order) for order in data]


