import datetime

from Ticket import Ticket
from BankAccount import BankAccount


class Carrier:

    __list_tickets = []

    def __init__(self, id_: int, places: int, price: float, card_number: int):
        self.__id = id_
        self.__places = places
        self.__price = price
        self.__card_number = card_number
        self.__bank_account = BankAccount(card_number, 0)
        for i in range(places):
            self.__list_tickets.append(Ticket(price, i, i + 1, date_time=datetime.datetime.now(), is_valid=True))

    def get_id(self):
        return self.__id

    def set_id(self, id_: int):
        self.__id = id_

    def get_places(self):
        return self.__places

    def set_places(self, places: int):
        self.__places = places

    def get_price(self):
        return self.__price

    def set_price(self, price: float):
        self.__price = price

    def get_card_number(self):
        return self.__card_number

    def set_card_number(self, card_number: int):
        self.__card_number = card_number

    def get_bank_account(self):
        return self.__bank_account

    def set_bank_account(self, bank_account: BankAccount):
        self.__bank_account = bank_account

    def get_list_tickets(self):
        return self.__list_tickets

    def accepting_funds(self, price: float):
        self.__bank_account.accepting_funds(price)

    def __str__(self):
        return f'id={self.__id}, ' \
               f'bank_account={self.__bank_account}, ' \
               f'list_tickets={self.__list_tickets}'
