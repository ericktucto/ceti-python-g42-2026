from sqlmodel import SQLModel, Field

class Producto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=False)
    precio: float = Field(index=False)
    disponible: bool = Field(default=True)
