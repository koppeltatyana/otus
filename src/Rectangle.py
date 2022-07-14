from src.Figure import Figure


class Rectangle(Figure):
    NAME = 'Rectangle'

    def __init__(self, a, b):
        if a < 0 or b < 0:
            raise ValueError("Все стороны прямоугольника должны быть положительными числами.")
        self.a = a
        self.b = b

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)

    @property
    def area(self):
        return self.a * self.b
