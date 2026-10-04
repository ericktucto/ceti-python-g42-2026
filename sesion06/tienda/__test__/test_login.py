from fastapi.testclient import TestClient


def test_health(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hola mundo"}

def test_login(client: TestClient):
    email = 'erick@ericktucto.com'
    password = 'secreto'
    response = client.post('/api/v1/auth/login', json={
        "correo": email,
        "password": password,
    })

    assert response.status_code == 200
    assert type(response.json()['token']) is str

