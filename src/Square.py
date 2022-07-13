from src.Figure import Figure


class Square(Figure):
    NAME = 'Square'

    def __init__(self, a):
        if a < 0:
            raise ValueError("Стороны квадрата должны быть положительными числами.")
        self.a = a

    @property
    def perimeter(self):
        return 4 * self.a

    @property
    def area(self):
        return self.a ** 2
