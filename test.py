import pytest
from app import app

def test_add():
    assert app.add(2, 3) == 5

def test_divide():
    assert app.divide(6, 3) == 2
