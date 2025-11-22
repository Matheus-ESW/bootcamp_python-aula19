from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import prodModel, db_test
from typing import List, Union
from prodSchema import Prod, ProdBase, ProdCreate

app = FastAPI()
prodModel.Base.metadata.create_all(bind=db_test.engine)

@app.get("/")
def home():
    return("Criando primeira API com FastAPI!! API criada pelo Matheus.")

@app.post("/prods/", response_model=Prod)
def create_prod(prod: ProdCreate, db: Session = Depends(db_test.get_db_test)):
    db_prod = prodModel.Prod(**prod.dict())
    db.add(db_prod)
    db.commit()
    db.refresh(db_prod)

    return db_prod

@app.get("/prods/", response_model=List[Prod])
def read_prods(skip: int = 0, limit: int = 10, db: Session = Depends(db_test.get_db_test)):
    prods = db.query(prodModel.Prod).offset(skip).limit(limit).all()

    return prods

@app.get("/prods/{prod_id}", response_model=Prod)
def read_prod(prod_id: int, db: Session = Depends(db_test.get_db_test)):
    db_prod = db.query(prodModel.Prod).filter(prodModel.Prod.prod_id == prod_id).first()

    if db_prod is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado!!")
    
    return db_prod

@app.put("/prods/{prod_id}", response_model=Prod)
def update_prod(prod_id: int, prod: ProdCreate, db: Session = Depends(db_test.get_db_test)):
    db_prod = db.query(prodModel.Prod).filter(prodModel.Prod.prod_id == prod_id).first()

    if db_prod is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado!!")
    
    for key, value in prod.dict().items():
        setattr(db_prod, key, value)

    db.commit()
    db.refresh(db_prod)
    
    return db_prod

@app.delete("/prods/{prod_id}", response_model=Prod)
def delete_prod(prod_id: int, db: Session = Depends(db_test.get_db_test)):
    db_prod = db.query(prodModel.Prod).filter(prodModel.Prod.prod_id == prod_id).first()

    if db_prod is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado!!")
    
    db.delete(db_prod)
    db.commit()
    
    return db_prod