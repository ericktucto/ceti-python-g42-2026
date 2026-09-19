ARCHIVO='tareas.txt'

def agregar_tarea(tareas, texto):
    """Agregar tarea a lista"""
    tareas.append({
        "texto": texto,
        "hecha": False
    })

def guardar_tareas(tareas):
    """Guardar las tareas en un archivo"""
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for tarea in tareas:
            estado = "1" if tarea["hecha"] else "0"
            archivo.write(f"{estado}|{tarea['texto']}\n")

def cargar_tareas():
    """Cargar las tareas en un archivo"""
    tareas = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue

                estado, texto = linea.split("|")
                tareas.append({
                    "texto": texto,
                    "hecha": estado == "1"
                })
    except FileNotFoundError:
        print("No existe el archivo de tareas")
    return tareas


def listar_tareas(tareas):
    """Lista las tareas en pantalla usando este formato
    # 1. [ ] o [x] <texto>
    """
    contador = 1
    for tarea in tareas:
        corchetes = "[x]" if tarea["hecha"] else "[ ]"
        print(f"{contador}. {corchetes} {tarea['texto']}")
        contador += 1


def marcar_tarea(tareas, marcar: int):
    indice = marcar - 1
    if indice < 0 or marcar > len(tareas):
        print("No existe esa tarea")
        return None

    tareas[indice]["hecha"] = not tareas[indice]["hecha"]
    print("Tarea marcada como completada")

