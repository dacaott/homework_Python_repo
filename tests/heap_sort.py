import pytest
from src.heap_sort import heap_sort


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([4, 3, 2, 0, -1, 4, 3], [-1, 0, 2, 3, 3, 4, 4]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        (
            [5, 4, 1, 13, 345, 1, 403, -14, -5, 1],
            [-14, -5, 1, 1, 1, 4, 5, 13, 345, 403],
        ),
        ([], []),
        ([1], [1]),
        ([-10, -2, -3, -9, -5, -3, -4], [-10, -9, -5, -4, -3, -3, -2]),
    ],
)
def test_basic(input_list, expected):
    assert heap_sort(input_list.copy()) == expected


def test_with_random(random_array):
    assert heap_sort(random_array.copy()) == sorted(random_array)
