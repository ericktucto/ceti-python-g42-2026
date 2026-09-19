from productos import cargar_productos, ver_productos
from carrito import agregar_producto, ver_carrito, quitar_producto, pagar, SaldoInsuficienteError
import random

def mostrar_menu():
    print("\n=== TIENDA VIRTUAL ===")
    print("1. Ver productos")
    print("2. Agregar al carrito")
    print("3. Quitar del carrito")
    print("4. Ver carrito")
    print("5. Pagar")
    print("6. Salir")

def obtener_un_numero(mensaje: str) -> int:
    while True:
        opcion = input(f"{mensaje}: ")
        try:
            opcion = int(opcion)
        except ValueError:
            print("La opcion no es valida")
            continue
        else:
            return opcion

def preguntar():
    while True:

        nombre = input("¿Como te llamas? ")
        nombre = nombre.strip()

        if not nombre:
            print("Debes escribir tu nombre")
            continue

        return nombre

def main():
    lista_productos = cargar_productos()
    nombre = preguntar()
    saldo = random.randint(5, 10)
    carrito = []
    print(f"\nBienvenido, {nombre}! Saldo: {saldo}")

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")
        try:
            opcion = int(opcion)
        except ValueError:
            print("La opcion no es valida")
            continue
        if opcion == 1:
            ver_productos(lista_productos)
            continue
        elif opcion == 2:
            ver_productos(lista_productos)
            n = obtener_un_numero("Elige un producto")
            agregar_producto(carrito, lista_productos, n)
            continue
        elif opcion == 3:
            ver_carrito(carrito)
            n = obtener_un_numero("Elige un producto para quitarlo")
            quitar_producto(carrito, n - 1)
            continue
        elif opcion == 4:
            ver_carrito(carrito)
            continue
        elif opcion == 5:
            try:
                saldo = pagar(carrito, saldo)
            except SaldoInsuficienteError as e:
                print(e)
            else:
                print(f"Tu saldo es S/ {saldo}")
                carrito = []
                print("Carrito vacio")
            continue
        elif opcion == 6:
            print("!Gracias por tu visita!")
            break
        else:
            print("La opcion no es valida")
            continue
        break

main()
