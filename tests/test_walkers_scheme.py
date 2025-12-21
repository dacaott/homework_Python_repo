import pytest
from src.test_2.walkers_scheme import WalkerScheme


def test_empty():
    with pytest.raises(ValueError):
        WalkerScheme([])


def test_negative_prob():
    with pytest.raises(ValueError):
        WalkerScheme([("a", 0.5), ("b", -0.1)])


def test_not_one_sum():
    with pytest.raises(ValueError):
        WalkerScheme([("a", 0.3), ("b", 0.3)])  # суммарно 0.6


def test_returns_valid_event():
    scheme = WalkerScheme([("a", 0.5), ("b", 0.5)])
    # Проверка случайного выбора
    for _ in range(10):
        event = scheme.get_random()
        assert event in ("a", "b")
