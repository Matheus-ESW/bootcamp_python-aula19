from pydantic import BaseModel
from typing import Union

class ProdBase(BaseModel):
    prod_name: str
    prod_price: float
    is_offer: Union[bool, None] = None

class ProdCreate(ProdBase):
    pass

class Prod(ProdBase):
    prod_id: int