from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    Type = "Квадрат"

    @classmethod
    def getType(self):
        return self.Type

    def __init__(self, color_param, side_param):
        self.side = side_param
        super().__init__(color_param, self.side, self.side)

    def __repr__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            self.getType(),
            self.fcolor.colorprop,
            self.side,
            self.square()
            )