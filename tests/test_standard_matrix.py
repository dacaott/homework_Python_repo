from src.test_number_2.standard_matrix import Matrix


def test_add():
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    assert (a + b) == Matrix([[6, 8], [10, 12]])


def test_scalar_mul():
    a = Matrix([[1, 2], [3, 4]])
    assert (a * 2) == Matrix([[2, 4], [6, 8]])
    assert (2 * a) == Matrix([[2, 4], [6, 8]])


def test_matrix_mul():
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    b = Matrix([[7, 8], [9, 10], [11, 12]])
    assert (a * b) == Matrix([[58, 64], [139, 154]])


def test_det():
    a = Matrix([[1, 2], [3, 4]])
    assert a.determinant() == -2


def test_iter():
    a = Matrix([[1, 2], [3, 4]])
    assert list(a) == [[1, 2], [3, 4]]
