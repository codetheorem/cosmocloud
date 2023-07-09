from typing import Annotated
from datetime import date, datetime, time, timedelta
from fastapi import Body, FastAPI
from pydantic import BaseModel

class UserAddress(BaseModel):
    city: str = None
    country: str = None
    zip_code: str = None

class Item(BaseModel):
    product_id: str = None
    bought_quantity: int = None

class Order(BaseModel):
    created_at: datetime = None
    items: list[Item] = []
    total_amount: float = None
    user_address: UserAddress

def order_serializer(order):
    return { 
            "id": str(order.get('_id')),
            "items": list(order.get('items')),
            "total_amount": float(order.get("total_amount")),
            "user_address": dict(order.get('user_address'))
    }