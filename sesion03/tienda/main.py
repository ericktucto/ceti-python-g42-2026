from productos import cargar_productos
import random

def mostrar_menu():
    print("\n=== TIENDA VIRTUAL ===")
    print("1. Ver productos")
    print("2. Agregar al carrito")
    print("3. Quitar del carrito")

def main():
    lista_tareas = cargar_productos()

    while True:
        print(lista_tareas)
        mostrar_menu()
        opcion = input("Elige una opcion: ")
        try:
            opcion = int(opcion)
        except ValueError:
            print("La opcion no es valida")
            continue
        if opcion == 1:
            pass
        elif opcion == 2:
            # 1. [ ] o [x] <texto>
            pass
        elif opcion == 3:
            # 1. [ ] o [x] <texto>
            pass
        elif opcion == 4:
            pass
        else:
            print("La opcion no es valida")
            continue
        break

main()
