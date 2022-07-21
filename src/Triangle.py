from src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    NAME = 'Triangle'

    def __init__(self, a, b, c):
        if a + b < c or a + c < b or b + c < a:
            raise ValueError("Для существования треугольника необходимо чтобы сумма его любых "
                             "двух сторон была больше третьей.")
        elif a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Все стороны треугольника должны быть положительными числами.")
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        semiperimeter = self.perimeter / 2
        return sqrt(semiperimeter * (semiperimeter - self.a) * (semiperimeter - self.b) * (semiperimeter - self.c))
