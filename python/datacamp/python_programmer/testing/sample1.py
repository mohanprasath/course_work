import pytest

def square(num: int) -> int:
    return num * num

def test_square():
    assert square(2) == 4
    assert square(0) == 0
    assert square(-2) == 4

