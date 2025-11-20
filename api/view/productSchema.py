from pydantic import BaseModel, PositiveFloat, PositiveInt
from typing import Union

class ProductSchema(BaseModel):
    product_name: str
    product_price: PositiveFloat
    is_offer: Union[bool, None] = None

class ProductCreate(ProductSchema):
    pass

class Product(ProductSchema):
    id: PositiveInt

class Config:
    from_attributes = True