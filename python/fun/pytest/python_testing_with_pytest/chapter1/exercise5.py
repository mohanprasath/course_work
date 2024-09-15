import pytest

def test_exercise5a():
    assert 1 in [2, 3, 4]

def test_exercise5b(a = 1, b=2):
    assert a < b

def test_exercise5c():
    assert 'fizz' not in 'fizzbuzz'
