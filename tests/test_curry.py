import pytest
from src.curry import curry, uncurry


def sum3(x, y, z):
    return x + y + z


def mul2(a, b):
    return a * b


def test_curry_sum3():
    sum3_c = curry(sum3, 3)
    assert sum3_c(1)(2)(3) == 6
    assert sum3_c(0)(0)(0) == 0
    assert sum3_c(-1)(2)(3) == 4


def test_uncurry_sum3():
    sum3_c = curry(sum3, 3)
    sum3_u = uncurry(sum3_c, 3)
    assert sum3_u(1, 2, 3) == 6
    assert sum3_u(3, 3, 3) == 9


def test_curry_mul2():
    mul2_c = curry(mul2, 2)
    assert mul2_c(2)(5) == 10


def test_uncurry_mul2():
    mul2_c = curry(mul2, 2)
    mul2_u = uncurry(mul2_c, 2)
    assert mul2_u(4, 5) == 20


def test_chain_equality():
    f = sum3
    f_curried = curry(f, 3)
    f_uncurried = uncurry(f_curried, 3)
    for x, y, z in [(1, 2, 3), (0, 5, 10), (-1, 1, 0)]:
        assert f(x, y, z) == f_uncurried(x, y, z)


def test_invalid_n_values():
    with pytest.raises(AssertionError):
        curry(sum3, -1)
    with pytest.raises(AssertionError):
        uncurry(sum3, -2)
    with pytest.raises(AssertionError):
        curry(sum3, 1.5)


def test_zero_arity_behavior():
    def f():
        return 42

    f_c = curry(f, 0)
    f_u = uncurry(f_c, 0)
    assert f_c() == 42
    assert f_u() == 42
