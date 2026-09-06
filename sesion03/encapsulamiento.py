class Cliente:
    def __init__(self, nombre, apellido, saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.__saldo = saldo

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    @property
    def saldo(self):
        """Un getter retorna los datos de un objecto"""
        return self.__saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        """Un setter sirve para cambiar los datos internos de mis objectos"""
        if type(nuevo_saldo) != int:
            return
        self.__saldo = nuevo_saldo if nuevo_saldo >= 0 else 0


c1 = Cliente("Juan", "Torres", 500)
# no debes acceder a las atributos que empiecen con _
#c1.__saldo = 0
#print(c1.__saldo)

print(c1.saldo)
print(c1.nombre_completo)

nuevo_saldo = -10

c1.saldo = nuevo_saldo

print(c1.saldo)
