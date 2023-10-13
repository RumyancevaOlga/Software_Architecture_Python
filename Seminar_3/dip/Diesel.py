from Engine import Engine


class Diesel(Engine):

    def __init__(self, horsepower: int):
        self.__horsepower = horsepower

    def get_horsepower(self):
        return self.__horsepower

    def set_horsepower(self, horsepower: int):
        self.__horsepower = horsepower

    def start(self) -> str:
        return 'start diesel engine'
