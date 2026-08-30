contador = 0

while contador <= 20:
    if contador % 3 == 0:
        print("es multiplo de 3", contador)
        contador = contador + 1
        continue
    print("solo el numero", contador)
    contador = contador + 1

print("-" * 15)


for numero in range(1, 6):
    print("Tu numero es -> ", numero)


for numero in range(6):
    print("-> ", numero)


for numero in range(13, 21):
    print("---> ", numero)

for numero in range(13, 21):
    if numero == 18:
        break
    print("@@@ -> ", numero)

print("Fin del archivo")