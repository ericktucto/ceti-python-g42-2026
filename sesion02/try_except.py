edad = 0
while True:
    try:
        edad = int(input("¿Cual es tu edad? "))
        break
    except ValueError:
        print("Coloca tu edad solo usando numeros")

print("edad ", edad)
