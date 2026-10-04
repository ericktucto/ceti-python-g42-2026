from fastapi import APIRouter
from fastapi.responses import JSONResponse

from tienda.docs.annotated.input.producto import NuevoProductoAnnotated
from tienda.repositories.producto import ProductoRepository
from tienda.schemas.input.producto import ActualizaProducto
from tienda.schemas.output.generic import NotFoundResource
from tienda.schemas.output.producto import Producto, ProductoGuardado
from tienda.db import SessionDep

router = APIRouter(prefix="/api/v1/productos", tags=["Productos"])

@router.get("/")
def todos_los_productos(session: SessionDep):
    repository = ProductoRepository(session)
    return repository.todos_los_productos()


@router.post("/", response_model=ProductoGuardado)
def guardar_producto(
        producto: NuevoProductoAnnotated,
        session: SessionDep
    ):
    repository = ProductoRepository(session)
    nuevo_producto = repository.guardar_producto(producto)
    return nuevo_producto


@router.get("/{id}", responses={
    200: {"model": Producto},
    404: {"model": NotFoundResource}
})
def obtener_producto(session: SessionDep, id: int):
    repository = ProductoRepository(session)
    producto = repository.obtener_producto(id)
    if producto is None:
        return JSONResponse(
                status_code=404,
                content={"message": "producto no encontrado"}
        )

    return producto


@router.put("/{id}", responses={
    200: {"model": Producto},
    404: {"model": NotFoundResource}
})
def actualizar_producto(id: int, session: SessionDep, producto: ActualizaProducto):
    repository = ProductoRepository(session)
    producto_db = repository.actualizar_producto(id, producto)
    if producto_db is None or producto_db.id is None:
        return JSONResponse(
                status_code=404,
                content={"message": "producto no encontrado"}
        )

    return Producto(id=producto_db.id,
                   nombre=producto_db.nombre,
                   precio=producto_db.precio,
                   disponible=producto_db.disponible)


@router.delete("/{id}", responses={
    200: {"model": Producto},
    404: {"model": NotFoundResource}
})
def eliminar_producto(id: int, session: SessionDep):
    repository = ProductoRepository(session)
    resultado = repository.eliminar_producto(id)
    if type(resultado) == bool or resultado.id is None:
        return JSONResponse(
                status_code=404,
                content={"message": "producto no encontrado"}
        )
    return Producto(id=resultado.id,
                   nombre=resultado.nombre,
                   precio=resultado.precio,
                   disponible=resultado.disponible)
