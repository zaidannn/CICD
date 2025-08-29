import pytest
from app import main

def test_add():
    assert main.add(2, 3) == 5

def test_divide():
    assert main.divide(6, 3) == 2
