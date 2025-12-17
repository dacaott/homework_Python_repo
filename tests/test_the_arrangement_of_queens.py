from src.the_arrangement_of_queens.enumeration import (
    count_queen_arrangements_enumeration,
)
from src.the_arrangement_of_queens.recursive import count_queen_arrangements_recursive


def test_enumeration():
    assert count_queen_arrangements_enumeration(4) == 2
    assert count_queen_arrangements_enumeration(8) == 92


def test_recursive():
    assert count_queen_arrangements_recursive(4) == 2
    assert count_queen_arrangements_recursive(8) == 92
