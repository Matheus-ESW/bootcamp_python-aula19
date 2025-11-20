from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from api.data.db import Base

class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)
    product_price = Column(Float)
    product_insert = Column(DateTime, default=func.now())