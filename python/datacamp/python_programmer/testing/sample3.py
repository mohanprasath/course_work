import pytest

def get_length(string):
    return len(string)
# The test marker syntax

@pytest.mark.skip
def test_get_len():
    assert get_length('123') == 3


def gen_sequence(n):
    return list(range(1, n+1))
# The xfail marker example

@pytest.mark.xfail
def test_gen_seq():
    assert gen_sequence(-1)


# The skipif marker example
@pytest.mark.skipif('2 * 2 == 5')
def test_get_len():
    assert get_length('abc') ==3
    assert get_length('xyz') == 3