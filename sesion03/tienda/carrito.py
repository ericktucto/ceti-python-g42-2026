from typing import List

from productos import Producto

class SaldoInsuficienteError(Exception):
    pass

def agregar_producto(
    carrito: List[Producto],
    productos: List[Producto],
    productoId: int
):
    for p in productos:
        if p.id == productoId:
            carrito.append(p)
            return None

def ver_carrito(carrito: List[Producto]):
    contador = 1
    print("---- CARRO DE COMPRAS ----")
    for producto in carrito:
        print(f"{contador}. {producto.nombre} - S/ {producto.precio}")
        contador += 1

def quitar_producto(
    carrito: List[Producto],
    indice: int
):
    if 0 <= indice < len(carrito):
        carrito.pop(indice)
    else:
        print("El producto no esta en el carrito")


def obtener_total(carrito: List[Producto]):
    return sum([p.precio for p in carrito])


def pagar(carrito: List[Producto], saldo: float):
    total = obtener_total(carrito)

    if saldo < total:
        raise SaldoInsuficienteError(f"El saldo es insuficiente. Saldo: {saldo}")

    print(f"El total a pagar es S/ {total}")
    return saldo - total


