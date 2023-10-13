from Quadrangle import Quadrangle


class Square(Quadrangle):

    def __init__(self, length: int):
        self.__length = length

    def get_length(self):
        return self.__length

    def set_length(self, length: int):
        self.__length = length

    def area(self) -> int:
        return self.__length * self.__length
