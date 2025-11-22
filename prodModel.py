from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Prod(Base):
    __tablename__ = 'prods'

    prod_id = Column(Integer, primary_key=True, index=False)
    prod_name = Column(String, index=False)
    prod_price = Column(Float)
    is_offer = Column(String, nullable=True)