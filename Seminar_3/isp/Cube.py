from Shape import Shape
from Shape3D import Shape3D


class Cube(Shape, Shape3D):
    def __init__(self, length: int):
        self.__length = length

    def get_length(self):
        return self.__length

    def set_length(self, length: int):
        self.__length = length

    def area(self) -> int:
        return 6 * self.__length ** 2

    def perimetr(self) -> float:
        return 12 * self.__length

    def volume(self) -> float:
        return self.__length ** 3
