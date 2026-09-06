from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio: int

#class Producto:
#    def __init__(self, nombre, precio):
#        self.nombre = nombre
#        self.precio = precio
#
#    def __str__(self):
#        return f"Producto(nombre='{self.nombre}', precio={self.precio})"

p1 = Producto("iPhone 15 Pro", 3500)
print(str(p1) + " <---")

@dataclass
class Cliente:
    nombre: str
    email: str
    _saldo: str

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor


c1 = Cliente("Ana", "ana@gmail.com", 2000)

print(c1.saldo)

c1.saldo = 100

print(c1.saldo)
