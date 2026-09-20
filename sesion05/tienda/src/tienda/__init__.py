from fastapi import FastAPI

from tienda.routers import productos

app = FastAPI()

@app.get("/")
def hola():
    return {"message": "hola mundo"}


@app.get("/search")
def buscar(q: str, type: str):
    pass

# PRODUCTOS
app.include_router(router=productos.router)
