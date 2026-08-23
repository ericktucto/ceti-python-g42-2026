edad = int(input("Dime tu edad: "))
estudiante = input("Escribe 's' si eres estudiante: ")

# SOLO PUEDEN ENTRAR A LA CLASE DE NATACION
# QUIENES SON MAYORES DE EDAD Y SON ESTUDIANTES

if edad >= 18 and estudiante == 's':
    print('AND: Puedes entrar al club de natacion')
else:
    print('AND: No puedes inscribirte')



if edad >= 18 or estudiante == 's':
    print('OR: Puedes entrar al club de natacion')
else:
    print('OR: No puedes inscribirte')