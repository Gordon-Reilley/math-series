import pytest
# from package_name.module.name import function_name
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series
# pytest tests must start with the "test_"
# must have two lines between functions
def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_6():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected


def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_6():
    actual = lucas(6)
    expected = 18
    assert actual == expected


def test_sum_series_0():
    actual = sum_series(0)
    expected = 3
    assert actual == expected


def test_sum_series_1():
    actual = sum_series(1)
    expected = 2
    assert actual == expected


# 3, 2, 5, 7, 12, 19, 31, 50
def test_sum_series_6():
    actual = sum_series(6)
    expected = 31
    assert actual == expected