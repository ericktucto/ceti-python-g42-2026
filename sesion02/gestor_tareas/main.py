from tareas import agregar_tarea, guardar_tareas, cargar_tareas, listar_tareas, marcar_tarea

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
        # Comprobar si eligió Agregar una tarea
        if opcion == 1:
            texto = input("Escribe tu nueva tarea: ")
            agregar_tarea(lista_tareas, texto)
            continue
        # Comprobar si eligió Listar las tareas
        elif opcion == 2:
            listar_tareas(lista_tareas)
            continue
        # Comprobar si eligió Marcar una como completada
        elif opcion == 3:
            listar_tareas(lista_tareas)
            marcar = input("Elige una tarea, para marcar como completada: ")
            try:
                marcar = int(marcar)
            except ValueError:
                print("La tarea no existe")
                continue
            marcar_tarea(lista_tareas, marcar)
            continue
        # Comprobar si eligió Salir y guardar
        elif opcion == 4:
            guardar_tareas(lista_tareas)
            print("Tareas guardadas")
            break
        else:
            print("La opcion no es valida")
            continue
        break

main()
