import pytest
import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, DevOps!" in response.data

def test_add(client):
    response = client.get("/add?a=2&b=3")
    data = response.get_json()
    assert data["result"] == 5

def test_add_invalid(client):
    response = client.get("/add?a=abc&b=3")
    assert response.status_code == 400
