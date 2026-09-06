class Notificable:
    def notificar(self):
        return f"notificando"

class Cliente(Notificable):
    def notificar(self):
        return f"enviando mensaje por whatsapp"

class Empresa(Notificable):
    def notificar(self):
        return f"enviando correo"

cliente = Cliente()
empresa = Empresa()

print(cliente.notificar())
print(empresa.notificar())