from pydantic import BaseModel

class NuevoProducto(BaseModel):
    nombre: str
    precio: float
    disponible: bool = True

class ActualizaProducto(BaseModel):
    nombre: str
    precio: float
    disponible: bool


