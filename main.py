import json
from typing import Union
from fastapi import FastAPI, Body
from pymongo import MongoClient
from entities.product import Product, ProductPydantic
from entities.order import Order, toJson
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from typing import Annotated



app = FastAPI()

client = MongoClient('mongodb+srv://hrishikeshagarwalv:Harsh2000@cluster0.c0onhzq.mongodb.net/?retryWrites=true&w=majority')

db = client.ecommerce_db


@app.get("/products/")
def get_all_products():
    data = list(db.products.find({}))
    return [Product(product).toJson() for product in data]

@app.put("/products/{product_id}")
def update_product(product_id: str, product: Annotated[dict, Body()]):
    product  = db.products.update_one({"_id": ObjectId(product_id)}, {"$set":product})
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
def get_orders(order_id: str, limit: int, offset: int):
    find_query = {}
    if order_id:
        find_query = {"_id": ObjectId(order_id)}
    data = list(db.orders.find(find_query), skip = offset, limit=limit)
    return [toJson(order) for order in data]


