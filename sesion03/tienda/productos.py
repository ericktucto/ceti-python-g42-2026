from dataclasses import dataclass
from typing import List
ARCHIVO='productos.txt'

@dataclass
class Producto:
    id: int
    nombre: str
    precio: float

def cargar_productos():
    """Cargar las productos en un archivo"""
    productos = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue

                id, nombre, precio = linea.split("|")
                p = Producto(int(id), nombre, float(precio))
                productos.append(p)
                
    except FileNotFoundError:
        print("No existe el archivo de productos")
    return productos


def ver_productos(productos: List[Producto]):
    contador = 1
    for producto in productos:
        print(f"{contador}. {producto.nombre} - S/ {producto.precio}")
        contador += 1

