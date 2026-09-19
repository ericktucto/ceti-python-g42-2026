try:
    # conexion = ConexionBaseDeDatos()
    n = int(
        input("Numero: ")
    )
    resultado = 10 / n
except ValueError:
    print("Eso no es un numero")
except ZeroDivisionError:
    print("No puedes dividir en cero")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Me ejecuto siempre")
    # conexion.close()