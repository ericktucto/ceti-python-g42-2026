# List comprehension
# [expresion bucle condicional]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
cuadrados = [n * n for n in numeros if n % 2 == 0]
print(cuadrados)

# Set comprehension
# {expresion bucle condicional}
numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
cuadrados2 = {a * a for a in numeros if a % 2 == 0}
print(cuadrados2)

compras_dolares = {
    "pan": 1,
    "manquilla": 3,
    "mermelada": 5
}

precios_soles = [valor * 3.5 for clave, valor in compras_dolares.items()]
print("precios en soles", precios_soles)

# Dict comprehension
# {clave: valor bucle condicional}

alumnos_notas = {
    "Ana": 18,
    "Mario": 11,
    "Maria": 10,
    "Carlos": 5,
    "David": 14,
    "Juan": 6
}

alumnos_aprobados = {
    nombre: nota
    for nombre, nota in alumnos_notas.items()
    if nota >= 11
}

print("Alumnos aprobados", alumnos_aprobados)
