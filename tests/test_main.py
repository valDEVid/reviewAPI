from fastapi.testclient import TestClient

from reviewAPI.main import app

client = TestClient(app)
user = {
    "username": "beta",
    "password": "1234"
}


def test_read_main():
    login = client.post("/login", data=user)
    assert login.status_code == 200
    header = {"Authorization": "Bearer " + login.json()["access_token"]}
    auth = client.get("/", headers=header)
    assert auth.status_code == 200
    products = client.get("/products")
    assert len(products.json()) >= 1