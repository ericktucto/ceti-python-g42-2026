from sqlmodel import SQLModel, Field

class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=False)
    correo: str = Field(index=True, unique=True)
    password: str = Field(index=False)
