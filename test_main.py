# test_main.py
from fastapi.testclient import TestClient
from test_main import app

client = TestClient(app)

def test_listar_produtos_sucesso():
    response = client.get("/produtos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)