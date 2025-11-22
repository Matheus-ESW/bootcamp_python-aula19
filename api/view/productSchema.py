from pydantic import BaseModel
from typing import Union

class ProductSchema(BaseModel):
    product_name: str
    product_price: float
    is_offer: Union[bool, None] = None

class ProductCreate(ProductSchema):
    pass

class Product(ProductSchema):
    product_id: int