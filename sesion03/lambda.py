def descuento(precio):
    return precio * 0.8


offer = lambda precio: precio * 0.8

print("descuento", descuento(200))
print("offer", offer(200))

descuento_aplicado = offer(150)

print(descuento_aplicado)
