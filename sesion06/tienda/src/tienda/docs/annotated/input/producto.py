from typing import Annotated

from fastapi import Body

from tienda.schemas.input.producto import NuevoProducto


NuevoProductoAnnotated = Annotated[
    NuevoProducto,
    Body(
        openapi_examples={
        "minimal": {
            "summary": "Datos minimos",
            "description": "Los datos minimos son el nombre y el precio",
            "value": {
                "nombre": "Teclado mecanico",
                "precio": 129.9
            }
        },
        "allowed": {
            "summary": "Configurando la disponibilidad",
            "description": "Configurando la disponibilidad",
            "value": {
                "nombre": "Mouse",
                "precio": 49.9,
                "disponible": False
            }
        }
    })
]


