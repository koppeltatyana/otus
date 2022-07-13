from math import pi, sqrt


class TestPerimeterAreaCalculations:
    """
    Тесты на проверку рассчета периметра и площади фигур
    """
    def test_triangle_area(self, additional_triangle_12_13_14):
        triangle = additional_triangle_12_13_14
        assert triangle.area() == sqrt((triangle.perimeter() / 2) *
                                       ((triangle.perimeter() / 2) - triangle.a) *
                                       ((triangle.perimeter() / 2) - triangle.b) *
                                       ((triangle.perimeter() / 2) - triangle.c))

    def test_triangle_perimeter(self, additional_triangle_12_13_14):
        triangle = additional_triangle_12_13_14
        assert triangle.perimeter() == triangle.a + triangle.b + triangle.c

    def test_rectangle_area(self, additional_rectangle_10_12):
        rectangle = additional_rectangle_10_12
        assert rectangle.area() == rectangle.a * rectangle.b

    def test_rectangle_perimeter(self, additional_rectangle_10_12):
        rectangle = additional_rectangle_10_12
        assert rectangle.perimeter() == 2 * (rectangle.a + rectangle.b)

    def test_square_area(self, additional_square_10):
        square = additional_square_10
        assert square.area() == square.a ** 2

    def test_square_perimeter(self, additional_square_10):
        square = additional_square_10
        assert square.perimeter() == square.a * 4

    def test_circle_area(self, additional_circle_10):
        circle = additional_circle_10
        assert circle.area() == pi * circle.r ** 2

    def test_circle_perimeter(self, additional_circle_10):
        circle = additional_circle_10
        assert circle.perimeter() == pi * circle.r * 2
