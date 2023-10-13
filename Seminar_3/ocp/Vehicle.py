class Vehicle:

    def __init__(self, max_speed: int, type_: str):
        self.__max_speed = max_speed
        self.__type = type_

    def get_max_speed(self) -> int:
        return self.__max_speed

    def get_type(self) -> str:
        return self.__type

    def calculate_al_lowed_speed(self) -> float:
        return self.__max_speed
