class Figure:
    NAME = None

    @property
    def area(self):
        return True

    @property
    def perimeter(self):
        return True

    def add_area(self, figure):
        return self.area() + figure.area()

    def __repr__(self):
        return f'Экземпляр класса "{self.NAME}"'
