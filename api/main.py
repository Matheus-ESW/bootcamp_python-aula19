from fastapi import FastAPI
from api.controller.productController import product_router

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Criando primeira API com FastAPI e usando rotas/modular!! API criada pelo Matheus."}

app.include_router(product_router)

# CONTROLLER = FUNÇÕES / NEGOCIO
# VIEW = VISUALIZAÇÃO / APLICAÇÃO
# MODEL = ATRIBUTOS / CLASSES