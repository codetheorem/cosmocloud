from pydantic import BaseModel

class ProductPydantic(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class Product:

    def __init__(self, o):
        self._o = o
    
    @property
    def name(self):
        return str(self._o['name'])
    
    @property
    def price(self):
        return self._o['price']
    
    @property
    def quantity(self):
        return int(self._o['quantity'])
    
    @property
    def id(self):
        return str(self._o['_id'])


    def toJson(self):
        return {
            "id": str(self._o.get('_id')),
            "name": str(self._o['name']),
            "price": self._o['price'],
            "quantity": int(self._o['quantity'])
        }