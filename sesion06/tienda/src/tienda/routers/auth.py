from fastapi import APIRouter
from starlette.responses import JSONResponse

from tienda import jwt
from tienda.db import SessionDep
from tienda.hashing import pwd
from tienda.repositories.usuario import UsuarioRepository
from tienda.schemas.input.auth import LoginUsuario, RegistroUsuario


router = APIRouter(prefix="/api/v1/auth", tags=["Autenticacion"])


@router.post("/register")
def register(datos_usuario: RegistroUsuario, session: SessionDep):
    repository = UsuarioRepository(session)
    usuario = repository.crear_usuario(datos_usuario)
    if usuario is None:
        return JSONResponse(
            status_code=422,
            content={
                "detail": "El correo ya esta registrado"
            }
        )

    return JSONResponse(
        content={
            "id": usuario.id,
            "correo": usuario.correo,
            "nombre": usuario.nombre,
        }
    )

@router.post("/login")
def login(datos_usuario: LoginUsuario, session: SessionDep):
    repository = UsuarioRepository(session)
    usuario = repository.obtener_usuario_por_correo(datos_usuario.correo)

    if usuario is None:
        return JSONResponse(
            status_code=422,
            content={
                "detail": "Credenciales invalidas"
            }
        )

    checked = pwd.verify(datos_usuario.password, usuario.password)

    if checked is False:
        return JSONResponse(
            status_code=422,
            content={
                "detail": "Credenciales invalidas"
            }
        )

    token = jwt.encode({
        "usuario_id": usuario.id
    })

    return JSONResponse(
        content={
            "token": token
        }
    )

@router.get("/me")
def me(session: SessionDep):
    pass

