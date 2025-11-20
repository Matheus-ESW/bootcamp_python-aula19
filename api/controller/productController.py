from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.data.db import engine, Base, get_db
from api.model.productModel import Product
from api.view.productSchema import ProductCreate

product_router = APIRouter(prefix="/product_router", tags=["Products"])
Base.metadata.create_all(bind=engine)

@product_router.post("/")
def home():
    print("Essa é a home")


@product_router.post("/items/", response_model=Product)
def create_product(product_data: ProductCreate, db: Session = Depends(get_db)):

    # monta o objeto ORM
    db_product = Product(**product_data.dict())

    # salva no banco
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product
