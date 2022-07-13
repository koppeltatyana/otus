from src.Figure import Figure
from math import pi


class Circle(Figure):
    NAME = 'Circle'

    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r ** 2

    def perimeter(self):
        return 2 * pi * self.r
