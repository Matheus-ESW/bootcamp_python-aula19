# DOS MEUS MODULOS
from api.model import productModel
from api.data import db
from api.view.productSchema import Product, ProductSchema, ProductCreate

# DEPENDENCIAS EXTERNAS
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Union

product_router = APIRouter(prefix="/prod_route", tags=["Products"])
productModel.Base.metadata.create_all(bind=db.engine)

@product_router.get("/prods", response_model=Product)
def return_all_products(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    prods = db.query(productModel,Product).offset(skip).limit(limit).all()

    return prods

@product_router.post("/prods", response_model=Product)
def create_product(prod: ProductCreate, db: Session = Depends(db.get_db)):
    db_prod = productModel.Product(**prod.dict())
    db.add(db_prod)
    db.commit()
    db.refresh(db_prod)

    return db_prod