from Engine import Engine
from Diesel import Diesel
from Patrol import Petrol


class Car:

    def __init__(self, engine: Engine):
        self.__engine = engine

    def get_engine(self):
        return self.__engine

    def start(self):
        return self.__engine.start()


# Как я поняла этот принцип, в класс закладывается абстракция, а при использовании экземпляра класса
# в него может забрасываться любая реализация этой абстракции

if __name__ == '__main__':
    car_1 = Car(Diesel(99))
    car_2 = Car(Petrol(120))
    print(f'{car_1.start()}, {car_2.start()}')
