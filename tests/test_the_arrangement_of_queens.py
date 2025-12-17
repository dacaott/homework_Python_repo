from src.the_arrangement_of_queens.enumeration import (
    count_queen_arrangements_enumeration,
)
from src.the_arrangement_of_queens.recursive import count_queen_arrangements_recursive


def test_enumeration():
    result = count_queen_arrangements_enumeration(4)
    assert isinstance(result, int)


def test_recursive():
    result = count_queen_arrangements_recursive(4)
    assert isinstance(result, int)
