import datetime


class Ticket:

    def __init__(self, price: float, id_: int, place: int, date_time: datetime.datetime, is_valid: bool):
        self.__price = price
        self.__id = id_
        self.__place = place
        self.__date_time = date_time
        self.__is_valid = is_valid

    def get_price(self):
        return self.__price

    def set_price(self, price: float):
        self.__price = price

    def get_id(self):
        return self.__id

    def set_id(self, id_: int):
        self.__id = id_

    def get_place(self):
        return self.__place

    def set_place(self, place: int):
        self.__place = place

    def get_date_time(self):
        return self.__date_time

    def set_date_time(self, date_time: datetime.datetime):
        self.__date_time = date_time

    def get_is_valid(self):
        return self.__is_valid

    def set_is_valid(self, is_valid: bool):
        self.__is_valid = is_valid

    def __str__(self):
        return f'id={self.__id}, ' \
               f'price={self.__price}, ' \
               f'place={self.__place}, ' \
               f'date_time={self.__date_time}, ' \
               f'is_valid={self.__is_valid}'

    def __repr__(self):
        return f'Ticket(id={self.__id}, ' \
               f'price={self.__price}, ' \
               f'place={self.__place}, ' \
               f'date_time={self.__date_time}, ' \
               f'is_valid={self.__is_valid})'
