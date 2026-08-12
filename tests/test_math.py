import pytest

# def test_one_plus_one():
#     assert 1+1 == 2

# def test_one_plus_two():
#     a = 1
#     b = 2 
#     c = 0
#     assert a + b == c

# def test_devide_by_zero():
#     num = 1/0


products = [
    (2,3,6),
    (1,99,99),
    (0,1,0),
    (3,-4,-12),
    (-5,-5,25),
    (2.5,6.7,16.75)
]

@pytest.mark.parametrize("a,b,expected", products)
def test_multiplication(a,b,expected):
    assert a * b == expected
