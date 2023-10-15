from BankAccount import BankAccount
from Ticket import Ticket


class User:

    def __init__(self, id_: int, user_name: str, hash_password: int, card_number: int):
        self.__id = id_
        self.__user_name = user_name
        self.__hash_password = hash_password
        self.__card_number = card_number
        self.__bank_account = BankAccount(card_number, 1000)
        self.__ticket = None

    def get_id(self):
        return self.__id

    def set_id(self, id_: int):
        self.__id = id_

    def get_hash_password(self):
        return self.__hash_password

    def set_hash_password(self, hash_password: int):
        self.__hash_password = hash_password

    def get_user_name(self):
        return self.__user_name

    def set_user_name(self, user_name: str):
        self.__user_name = user_name

    def get_card_number(self):
        return self.__card_number

    def set_card_number(self, card_number: int):
        self.__card_number = card_number

    def get_bank_account(self):
        return self.__bank_account

    def set_bank_account(self, bank_account: BankAccount):
        self.__bank_account = bank_account

    def get_ticket(self):
        return self.__ticket

    def set_ticket(self, ticket: Ticket):
        self.__ticket = ticket

    def get_balance(self):
        return self.__bank_account.get_balance()

    def write_down(self, price: float):
        self.__bank_account.write_down(price)

    def __str__(self):
        return f'id={self.__id}, ' \
               f'user_name={self.__user_name}, ' \
               f'bank_account={self.__bank_account},' \
               f'ticket={self.__ticket}'
