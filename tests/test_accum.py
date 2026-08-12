import pytest
from stuff.accum import accumulator

@pytest.fixture
def accum():
    return accumulator()

def test_accumulator_init():
    acc = accumulator()
    assert acc.count == 0

def test_accumulator_add():
    acc = accumulator()
    acc.add()
    assert acc.count == 1

def test_accumulator_add_three():
    acc = accumulator()
    acc.add(3)
    assert acc.count == 3

def test_accumulator_add_twice():
    acc = accumulator()
    acc.add()
    acc.add()
    assert acc.count == 2

def test_accumulator_cannot_set_directly():
    acc = accumulator()
    with pytest.raises(AttributeError):
        acc.count = 10

