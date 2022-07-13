from src.Figure import Figure
from math import sqrt


class Triangle(Figure):
    NAME = 'Triangle'

    def __init__(self, a, b, c):
        if a + b < c or a + c < b or b + c < a:
            raise ValueError("Для существования треугольника необходимо чтобы сумма его любых "
                             "двух сторон была больше третьей.")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        semiperimeter = self.perimeter() / 2
        return sqrt(semiperimeter * (semiperimeter - self.a) * (semiperimeter - self.b) * (semiperimeter - self.c))
