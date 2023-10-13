from Shape import Shape


class Square(Shape):

    def __init__(self, length: int):
        self.__length = length

    def get_length(self):
        return self.__length

    def set_length(self, length: int):
        self.__length = length

    def area(self) -> int:
        return self.__length ** 2

    def perimetr(self) -> float:
        return 4 * self.__length
