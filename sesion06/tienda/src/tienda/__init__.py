from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from tienda.routers import productos, auth

app = FastAPI()

@app.get("/")
def hola():
    return {"message": "hola mundo"}


# PRODUCTOS
app.include_router(router=productos.router)

# AUTH
app.include_router(router=auth.router)
