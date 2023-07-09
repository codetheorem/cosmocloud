from pymongo import MongoClient

client = MongoClient('mongodb+srv://hrishikeshagarwalv:Harsh2000@cluster0.c0onhzq.mongodb.net/?retryWrites=true&w=majority')

db = client.ecommerce_db