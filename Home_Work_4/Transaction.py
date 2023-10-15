import datetime

from User import User
from Carrier import Carrier


class Transaction:

    def __init__(self, user: User, carrier: Carrier):
        self.__user = user
        self.__carrier = carrier

    def get_user(self):
        return self.__user

    def set_user(self, user: User):
        self.__user = user

    def get_carrier(self):
        return self.__carrier

    def set_carrier(self, carrier: Carrier):
        self.__carrier = carrier

    def bay_ticket(self, place: int):
        # предусловие стоимости билета и баланса покупателя
        if self.__user.get_balance() >= self.__carrier.get_price():
            for ticket in self.__carrier.get_list_tickets():
                # предусловие на свободное место
                if ticket.get_place() == place and ticket.get_is_valid() is True:
                    ticket.set_date_time(date_time=datetime.datetime.now())
                    self.__user.set_ticket(ticket)
                    self.__user.write_down(self.__carrier.get_price())
                    self.__carrier.accepting_funds(self.__carrier.get_price())
                    ticket.set_is_valid(False)
                elif ticket.get_place() == place and ticket.get_is_valid() is False:
                    print('Выберите свободное место')

    def __str__(self):
        return f'user={self.__user}, carrier={self.__carrier}'
