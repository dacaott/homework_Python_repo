import pytest
from src.the_arrangement_of_queens import enumeration, optimized, recursive


def test_enumeration_small():
    assert enumeration.count_queen_arrangements_enumeration(4) == 2


def test_optimized_small():
    assert optimized.count_queen_arrangements_optimized(4) == 2


def test_recursive_small():
    assert recursive.count_queen_arrangements_recursive(4) == 2


@pytest.mark.parametrize(
    "N, expected",
    [
        (1, 1),
        (2, 0),
        (3, 0),
        (4, 2),
    ],
)
def test_known_values(N, expected):
    assert enumeration.count_queen_arrangements_enumeration(N) == expected
    assert optimized.count_queen_arrangements_optimized(N) == expected
    assert recursive.count_queen_arrangements_recursive(N) == expected
