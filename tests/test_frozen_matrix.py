from src.test_number_2.frozen_matrix import FrozenMatrix


def test_equality():
    a = FrozenMatrix([[1, 2], [3, 4]])
    b = FrozenMatrix([[1, 2], [3, 4]])
    c = FrozenMatrix([[1, 2], [4, 3]])

    assert a == b
    assert a != c


def test_hashable():
    a = FrozenMatrix([[1, 2], [3, 4]])
    b = FrozenMatrix([[1, 2], [3, 4]])

    s = {a}
    assert b in s  # проверяем, что хэш + eq корректны


def test_can_be_dict_key():
    a = FrozenMatrix([[1, 2], [3, 4]])
    d = {a: "matrix"}

    assert d[a] == "matrix"


def test_indexing_and_iteration():
    m = FrozenMatrix([[10, 20], [30, 40]])

    assert m[0] == (10, 20)
    assert list(m) == [(10, 20), (30, 40)]
    assert len(m) == 2


def test_repr():
    m = FrozenMatrix([[1, 2]])
    assert "FrozenMatrix" in repr(m)
