import pytest
import random


@pytest.fixture
def random_array():
    length = random.randint(1, 100)
    arr = [random.randint(-10000, 10000) for _ in range(length)]
    print("\nСлучайный массив для теста:", arr)
    return arr
