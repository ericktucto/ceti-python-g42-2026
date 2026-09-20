from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    disponible: bool

class ProductoGuardado(BaseModel):
    id: int
    nombre: str
    precio: float
    disponible: bool

