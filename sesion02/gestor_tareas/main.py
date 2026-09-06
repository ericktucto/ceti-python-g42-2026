from tareas import agregar_tarea, guardar_tareas, cargar_tareas

def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir (guardando)")

def main():
    lista_tareas = cargar_tareas()

    while True:
        #print(lista_tareas)
        mostrar_menu()
        opcion = input("Elige una opcion: ")
        try:
            opcion = int(opcion)
        except ValueError:
            print("La opcion no es valida")
            continue
        if opcion == 1:
            texto = input("Escribe tu nueva tarea: ")
            agregar_tarea(lista_tareas, texto)
            continue
        elif opcion == 2:
            # 1. [ ] o [x] <texto>
            pass
        elif opcion == 3:
            # 1. [ ] o [x] <texto>
            pass
        elif opcion == 4:
            guardar_tareas(lista_tareas)
            print("Tareas guardadas")
            break
        else:
            print("La opcion no es valida")
            continue
        break

main()
