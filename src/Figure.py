class Figure:
    NAME = None

    @property
    def area(self):
        return True

    @property
    def perimeter(self):
        return True

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("В качестве параметра в функцию требуется передавать экземпляр фигуры.")
        return float(self.area) + float(figure.area)

    def __repr__(self):
        return f'Экземпляр класса "{self.NAME}"'
