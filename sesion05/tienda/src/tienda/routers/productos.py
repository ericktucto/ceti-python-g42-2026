from fastapi import APIRouter
from fastapi.responses import JSONResponse

from tienda.docs.annotated.input.producto import NuevoProductoAnnotated
from tienda.schemas.input.producto import ActualizaProducto
from tienda.schemas.output.generic import NotFoundResource
from tienda.schemas.output.producto import Producto, ProductoGuardado

router = APIRouter(prefix="/api/v1/productos", tags=["Productos"])

productos = []

@router.get("/")
def todos_los_productos():
    return productos


@router.post("/", response_model=ProductoGuardado)
def guardar_producto(
        producto: NuevoProductoAnnotated
    ):
    nuevo_producto = {
            "id": len(productos) + 1,
            "nombre": producto.nombre,
            "precio": producto.precio,
            "disponible": producto.disponible
    }
    productos.append(nuevo_producto)
    return nuevo_producto


@router.get("/{id}", responses={
    200: {"model": Producto},
    404: {"model": NotFoundResource}
})
def obtener_producto(id: int):
    for producto in productos:
        if producto["id"] == id:
            return producto
    return JSONResponse(
            status_code=404,
            content={"message": "producto no encontrado"}
    )


@router.put("/{id}", responses={
    200: {"model": Producto},
    404: {"model": NotFoundResource}
})
def actualizar_producto(id: int, producto: ActualizaProducto):
    for p in productos:
        if p["id"] == id:
            p["nombre"] = producto.nombre
            p["precio"] = producto.precio
            return producto
    return JSONResponse(
            status_code=404,
            content={"message": "producto no encontrado"}
    )


@router.delete("/{id}", responses={
    200: {"model": Producto},
    404: {"model": NotFoundResource}
})
def eliminar_producto(id: int):
    for producto in productos:
        if producto["id"] == id:
            productos.remove(producto)
            return producto
    return JSONResponse(
            status_code=404,
            content={"message": "producto no encontrado"}
    )
