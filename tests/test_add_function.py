import pytest


class TestPerimeterAreaCalculations:
    """
    Тесты на проверку функции "add_area"
    """
    def test_triangle_and_circle_add_area(self, additional_triangle_12_13_14, additional_circle_10):
        assert additional_circle_10.add_area(additional_triangle_12_13_14) == \
               additional_triangle_12_13_14.add_area(additional_circle_10)

    def test_triangle_and_rectangle_add_area(self, additional_triangle_12_13_14, additional_rectangle_10_12):
        assert additional_rectangle_10_12.add_area(additional_triangle_12_13_14) == \
               additional_triangle_12_13_14.add_area(additional_rectangle_10_12)

    def test_triangle_and_square_add_area(self, additional_triangle_12_13_14, additional_square_10):
        assert additional_square_10.add_area(additional_triangle_12_13_14) == \
               additional_triangle_12_13_14.add_area(additional_square_10)

    def test_rectangle_and_square_add_area(self, additional_rectangle_10_12, additional_square_10):
        assert additional_square_10.add_area(additional_rectangle_10_12) == \
               additional_rectangle_10_12.add_area(additional_square_10)

    def test_rectangle_and_circle_add_area(self, additional_rectangle_10_12, additional_circle_10):
        assert additional_circle_10.add_area(additional_rectangle_10_12) == \
               additional_rectangle_10_12.add_area(additional_circle_10)

    def test_square_and_circle_add_area(self, additional_square_10, additional_circle_10):
        assert additional_circle_10.add_area(additional_square_10) == \
               additional_square_10.add_area(additional_circle_10)

    def test_triangle_add_negative(self, additional_triangle_12_13_14):
        with pytest.raises(ValueError):
            additional_triangle_12_13_14.add_area('qwe')

    def test_rectangle_add_negative(self, additional_triangle_12_13_14):
        with pytest.raises(ValueError):
            additional_triangle_12_13_14.add_area('qwe')

    def test_circle_add_negative(self, additional_triangle_12_13_14):
        with pytest.raises(ValueError):
            additional_triangle_12_13_14.add_area('qwe')

    def test_square_add_negative(self, additional_triangle_12_13_14):
        with pytest.raises(ValueError):
            additional_triangle_12_13_14.add_area('qwe')
