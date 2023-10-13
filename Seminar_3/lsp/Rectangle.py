from Quadrangle import Quadrangle


class Rectangle(Quadrangle):

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width: int):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height: int):
        self.__height = height

    def area(self) -> int:
        return self.__width * self.__height
