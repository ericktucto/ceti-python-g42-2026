from abc import ABC, abstractmethod
# ABC
# Abstract Base Classes

class MetodoDePago(ABC):
    @abstractmethod
    def pagar(self):
        pass

class PagoConTarjeta(MetodoDePago):
    def pagar(self):
        return "Pagando con tarjeta"

class PagoConYape(MetodoDePago):
    def pagar(self):
        return "Haciendo yapeo"


pago_tarjeta = PagoConTarjeta()

print(pago_tarjeta.pagar())

def procesar_pedido(metodo_de_pago):
    print(metodo_de_pago.pagar())


procesar_pedido(PagoConYape())