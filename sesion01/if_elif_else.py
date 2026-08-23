edad = int(input("Dime tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
    print("Un linea mas")
else:
    print("Eres menor de edad")
    print("Prueba nuevamente")
print("Fuera de else")

nota = int(input("Escribe tu nota: "))

if nota >= 15:
    print("Aprobaste")
    print("Felicidades")
elif nota >= 11:
    print("Necesitas recuperar")
    print("Tomaras un nuevo examen")
elif nota >= 5:
    print("Tienes una mala nota")
else:
    print("Reprobaste")
