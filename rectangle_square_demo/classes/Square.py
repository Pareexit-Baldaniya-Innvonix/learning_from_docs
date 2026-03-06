from .Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_size):
        super().__init__(side_size, side_size)
