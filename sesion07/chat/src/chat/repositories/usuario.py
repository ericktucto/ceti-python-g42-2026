
from sqlmodel import select

from chat.db import SessionDep
from chat.hashing import pwd
from chat.models.usuario import Usuario
from chat.schemas.input.auth import RegistroUsuario


class UsuarioRepository():
    def __init__(self, session: SessionDep):
        self.session = session

    def crear_usuario(self, datos: RegistroUsuario) -> Usuario | None:
        usuario_correo = self.obtener_usuario_por_correo(datos.correo)

        if usuario_correo is not None:
            return None

        hashed_password = pwd.hash(datos.password)

        nuevo_usuario = Usuario(
            nombre=datos.nombre,
            correo=datos.correo,
            password=hashed_password,
        )

        self.session.add(nuevo_usuario)
        self.session.commit()
        return nuevo_usuario

    def obtener_usuario_por_correo(self, correo: str) -> Usuario | None:
        return self.session.exec(
            select(Usuario).where(Usuario.correo == correo)
        ).first()


