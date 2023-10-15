class BankAccount:

    def __init__(self, card_number: int, balance: float):
        self.__card_number = card_number
        self.__balance = balance

    def get_card_number(self):
        return self.__card_number

    def set_card_number(self, card_number: int):
        self.__card_number = card_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance: float):
        self.__balance = balance

    def write_down(self, cost: float):
        self.__balance -= cost

    def accepting_funds(self, funds: float):
        self.__balance += funds

    def __str__(self):
        return f'card_number={self.__card_number}, balance={self.__balance}'
