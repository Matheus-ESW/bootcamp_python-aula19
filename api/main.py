from fastapi import FastAPI
from api.controller.productController import product_router

app = FastAPI()
app.include_router(product_router)

# CONTROLLER = FUNÇÕES / NEGOCIO
# VIEW = VISUALIZAÇÃO / APLICAÇÃO
# MODEL = ATRIBUTOS / CLASSES