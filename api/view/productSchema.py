from pydantic import BaseModel

class ProductSchema(BaseModel):
    product_id: int
    product_name: str
    product_price: float

    class Config:
        from_attributes = True