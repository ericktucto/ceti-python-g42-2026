class Notificable:
    def notificar():
        return f"notificando"

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre}"


u1 = Usuario("Ana", 32)
u2 = Usuario("Pedro", 25)


print("nombre de usuario 1", u1.nombre)
print("edad de usuario 1", u1.edad)
print(u2.presentarse())


class Cliente(Notificable, Usuario):
    def __init__(self, nombre, edad, email, saldo):
        super().__init__(nombre, edad)
        self.email = email
        self.saldo = saldo

    def comprar(self):
        return f"{self.nombre} compra"


c1 = Cliente("Tom", 32, "tom@gmail.com", 1200)

print(Cliente.__mro__)

print(c1.presentarse())
print("Nombre de cliente 1", c1.nombre)
print(c1.comprar())