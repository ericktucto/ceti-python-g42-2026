def saludar(nombre):
    return f"Hola, {nombre}"

def hola(nombre):
    print(f"Hola, {nombre}")

mensaje = saludar("Erick")
print(mensaje)

salida = hola("Pepito")

print(salida, None)


x = 10
def f():
    y = 5
    print("y desde f", y)
    return x + y

print(f(), x)

# esto tira error por que y no esta
# definida,y esta definida solo en f
# print(y)

def area(
    base: float,
    altura: float
) -> float:
    """Calcular el area
    """
    return base * altura

print(area(7.2, 5.5))
print(area("7.2", 5))

