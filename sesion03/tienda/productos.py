from dataclasses import dataclass
ARCHIVO='productos.txt'

@dataclass
class Producto:
    id: int
    nombre: str
    precio: int

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
                p = Producto(int(id), nombre, int(precio))
                productos.append(p)
                
    except FileNotFoundError:
        print("No existe el archivo de productos")
    return productos
