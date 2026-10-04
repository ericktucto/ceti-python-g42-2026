from os import getenv
from typing import Annotated

from fastapi import Depends
from sqlmodel import create_engine, Session


# DATABASE_URL = "postgresql://<user>:<password>@<ip>:<port>/<database>"
# DATABASE_URL = "postgresql://erick:1234@localhost:5432/tienda"
DATABASE_URL=getenv('DATABASE_URL')

engine = create_engine(
    DATABASE_URL
)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
