import pytest

class Session():
    def close(self):
        pass

class Application():
    def get(self, url, data):
        pass

# tablas
# - productos
# - facturas
# - usuarios

@pytest.fixture
def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()



def test_hacer_una_compra_genera_una_factura(session_db: Session, app: Application):
    # inicio sesion
    # agrega productos al carrito
    # compra
    # revisar la factura creada

    compras = [
            {"producto_id": 1, "nombre": "teclado mecanico", "cantidad": 2},
    ]
    response = app.get("/api/comprar", compras)
    assert response.status_code == 200

    filas = session_db.exec("select * from productos where producto_id = 1")

    assert len(filas) == 1
    assert filas[0]["cantidad"] == 2
    assert filas[0]["producto_id"] == 1


@pytest.fixture
def app():
    # creacion de app y login
    pass

def test_total_de_compra_usando_cupon_de_descuento(app: Application):
    # agrega productos al carrito
    # agregar cupon
    # verificar en el carrito el nuevo precio
    pass
