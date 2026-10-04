from sqlmodel import select

from tienda.db import SessionDep
from tienda.docs.annotated.input.producto import NuevoProductoAnnotated
from tienda.models.producto import Producto
from tienda.schemas.input.producto import ActualizaProducto

# CRUD

class ProductoRepository():
    def __init__(self, session: SessionDep):
        self.session = session

    def todos_los_productos(self):
        return self.session.exec(
            select(Producto)
        ).all()


    def guardar_producto(self, producto: NuevoProductoAnnotated) -> Producto:
        nuevo_producto = Producto(
            nombre=producto.nombre,
            precio=producto.precio,
            disponible=producto.disponible
        )
        self.session.add(nuevo_producto)
        self.session.commit()
        return nuevo_producto

    def obtener_producto(self, id: int):
        return self.session.get(Producto, id)

    def actualizar_producto(self, id: int, producto: ActualizaProducto):
        producto_db = self.obtener_producto(id)
        if producto_db is None:
            return None
        producto_db.nombre = producto.nombre
        producto_db.precio = producto.precio
        producto_db.disponible = producto.disponible

        self.session.commit()

        return producto_db

    def eliminar_producto(self, id: int) -> Producto | bool:
        producto = self.obtener_producto(id)
        if producto is None:
            return False
        self.session.delete(producto)
        self.session.commit()
        return producto

