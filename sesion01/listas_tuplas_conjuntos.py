print("LISTAS")
print("-" * 15)

frutas = ["manzana", "pera", "kiwi"]

for fruta in frutas:
    print("Mi fruta es", fruta)

print(frutas)

frutas.append("naranja")

print(frutas)

frutas.insert(0, "mango")

print(frutas)

frutas.insert(2, "sandia")

print(frutas)

print(frutas[4])

print(frutas[-1])

# quiero obtener desde manzana hasta pera
print(frutas[1:3])
print(frutas[1:4])
# ----

print(frutas[:3])

print(frutas[2:])

print(frutas)
print("2", frutas[::2])
print("3", frutas[::3])

print("sandia 2", frutas[2::2])
print("manzana 3", frutas[1:5:3])

print(frutas[::-2])

eliminado = frutas.pop(2)
print("sin sandia", frutas, eliminado)

frutas[1] = "toronja"
print(frutas)

print("TUPLAS")
print("-" * 15)

numeros = (10, 20, 35, 92, 5)
#numeros.append(30)
#numeros[1] = 30
for n in numeros:
    print("Mi numero es", n)

numeros_revertidos = numeros[::-1]

print(numeros_revertidos)
print(numeros)

print("SET O CONJUNTOS")
print("-" * 15)

miconjunto = { 1, 2, 3, 2, 4, 30 }

print(miconjunto)

ciudades = set(["lima", "quito", "new york", "lima", "la paz"])

print(ciudades)

ciudades.add("madrid")

print(ciudades)

ciudades.remove("quito")

print(ciudades)

ciudades.pop()

print(ciudades)

ciudades.clear()

print(ciudades)