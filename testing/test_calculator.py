import calculator
import pytest


def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(2, 9) == 11


def test_sub():
    assert calculator.sub(2, 3) == -1
    assert calculator.sub(2, 9) == -7


def test_mul():
    assert calculator.mul(2, 3) == 6
    assert calculator.mul(2, 9) == 18


def test_div():
    assert calculator.div(2, 3) == 2 / 3
    assert calculator.div(2, 9) == 2 / 9


# more example's are coming soon
