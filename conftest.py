import pytest

from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Circle import Circle


@pytest.fixture
def additional_circle_10():
    return Circle(10)


@pytest.fixture
def additional_triangle_12_13_14():
    return Triangle(12, 13, 14)


@pytest.fixture
def additional_rectangle_10_12():
    return Rectangle(10, 12)


@pytest.fixture
def additional_square_10():
    return Square(10)
