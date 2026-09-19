from operaciones import suma

def test_funcion_suma_hace_una_suma():
    resultado = suma(11, 7)
    assert resultado == 18

