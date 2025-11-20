from fastapi import APIRouter
from api.data.db import SessionLocal, engine, Base
from api.model.productModel import Product
from api.view.productSchema import ProductSchema

product_router = APIRouter(prefix="/product_router", tags=["Products"])
Base.metadata.create_all(bind=engine)

@product_router.post("/items", response_model=ProductSchema)
def create_product(product_data: ProductSchema):

    db_product = Product(
        product_id=product_data.product_id,
        product_name=product_data.product_name,
        product_price=product_data.product_price
    )

    return db_product

def add_product_to_db(product_schema: ProductSchema) -> Product:

    with SessionLocal() as db:
    
        db_product = Product(product_id=product_schema.product_id, product_name=product_schema.product_name, product_price=product_schema.product_price)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)

        return db_product