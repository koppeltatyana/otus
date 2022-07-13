import pytest

from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Circle import Circle


class TestShapesInit:
    """
    Тесты для проверки создания фигур
    """
    def test_positive_triangle(self):
        assert Triangle(12, 13, 14)

    def test_negative_triangle(self):
        with pytest.raises(ValueError):
            Triangle(12, 13, 26)

    def test_negative_triangle_less_null(self):
        with pytest.raises(ValueError):
            Triangle(-12, 13, 26)

    def test_rectangle(self):
        assert Rectangle(10, 12)

    def test_rectangle_less_null(self):
        with pytest.raises(ValueError):
            Rectangle(-10, 12)

    def test_square(self):
        assert Square(10)

    def test_square_less_null(self):
        with pytest.raises(ValueError):
            Square(-10)

    def test_circle(self):
        assert Circle(10)

    def test_circle_less_null(self):
        with pytest.raises(ValueError):
            Circle(-10)
