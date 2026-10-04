from pydantic import BaseModel


class NotFoundResource(BaseModel):
    message: str = 'Recurso no encontrado'
