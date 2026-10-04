from tienda.models.usuario import Usuario
from tienda.hashing import pwd
from sqlmodel import SQLModel
from os import getenv
from sqlmodel import Session, create_engine
from fastapi.testclient import TestClient
import pytest

from tienda import app
from tienda.db import get_session

# OPCION A: En cada prueba
# 1. Tumbar todas las tablas
# 2. Crear todas las tablas o al menos las que necesites para tus pruebas
# 3. Llenar de informacion las tablas
# 4. Ejecutar tus pruebas
# 5. Eliminar las tablas (opcional)

# OPCION B(Recomendada): Basarse en transacciones, hace tu setup de base de datos antes de todas tus pruebas
# 1. Tumbar todas las tablas
# 2. Crear todas las tablas o al menos las que necesites para tus pruebas
# 3. Llenar de informacion las tablas
# 4. Ejecutar tus pruebas
# 4.1 Empezar un transaccion
# 4.2 Ejecutar la prueba
# 4.3 Terminando la pruebas haces un rollback
# 5. Eliminar las tablas (opcional)


TEST_DATABASE_URL = getenv('TEST_DATABASE_URL')
test_engine = create_engine(TEST_DATABASE_URL)


@pytest.fixture
def session():
    connection = test_engine.connect()
    transaction = connection.begin()
    s = Session(
        bind=connection,
        join_transaction_mode="create_savepoint"
    )
    try:
        yield s
    finally:
        s.close()
        transaction.rollback()
        connection.close()


@pytest.fixture
def client(session: Session):
    def get_test_session():
        yield session

    app.dependency_overrides[get_session] = get_test_session

    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    # construir todas las tablas
    SQLModel.metadata.create_all(test_engine)

    # llenar tablas
    seed_database()

    # Ejecutar todas las pruebas
    yield

    # Al terminar de ejecutar todas las pruebas, eliminamos las tablas
    SQLModel.metadata.drop_all(test_engine)

def seed_database():
    with Session(test_engine) as session:
        password_hash = pwd.hash('secreto')
        nuevo_usuario = Usuario(
            nombre='Erick Tucto Testing',
            correo='erick@ericktucto.com',
            password=password_hash
        )
        session.add(nuevo_usuario)
        session.commit()