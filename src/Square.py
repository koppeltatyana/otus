from src.Figure import Figure


class Square(Figure):
    NAME = 'Square'

    def __init__(self, a):
        self.a = a

    def perimeter(self):
        return 4 * self.a

    def area(self):
        return self.a ** 2
