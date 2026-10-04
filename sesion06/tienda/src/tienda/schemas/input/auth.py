from pydantic import BaseModel

class RegistroUsuario(BaseModel):
    nombre: str
    correo: str
    password: str

class LoginUsuario(BaseModel):
    correo: str
    password: str
