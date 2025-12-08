from src.test_number_2.mtx import serialize, deserialize


def test_serialize_deserialize():
    matrix = [[1, 2, 3], [4, 5, 6]]

    text = serialize(matrix)
    restored = deserialize(text)

    assert restored == matrix


def test_empty_matrix():
    matrix = []
    text = serialize(matrix)
    assert text == "0 0"
    restored = deserialize(text)
    assert restored == []


def test_non_rectangular_error():
    bad_matrix = [[1, 2], [3, 4, 5]]
    import pytest

    with pytest.raises(ValueError):
        serialize(bad_matrix)


def test_wrong_format():
    import pytest

    with pytest.raises(ValueError):
        deserialize("2 2\n1 2 3")


def test_float_values():
    matrix = [[1.5, 2.0], [3.25, 4.75]]
    text = serialize(matrix)
    restored = deserialize(text)
    assert restored == matrix
