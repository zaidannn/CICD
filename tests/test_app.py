import sys
import os
import pytest
import add
import divide

# tambahkan path root project (CICD)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app   # sekarang bisa import


# --- test fungsi langsung ---
def test_add_function():
    assert add(2, 3) == 5

def test_divide_function():
    assert divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

# --- test endpoint Flask ---
def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Hello, DevOps!"}

def test_add_route():
    client = app.test_client()
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json == {"result": 5}
