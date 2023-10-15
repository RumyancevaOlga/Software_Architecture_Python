from Carrier import Carrier
from User import User
from Transaction import Transaction


if __name__ == '__main__':
    carrier = Carrier(1, 20, 120.20, 1234_5678_9101_1121)
    print(carrier)
    user = User(1, 'Adam', 45454534534354534534534534545635, 1111_2222_3333_4444)
    print(user)
    transaction = Transaction(user, carrier)
    print(transaction)
    transaction.bay_ticket(2)
    print(transaction)
    transaction.bay_ticket(2)
    print(transaction)
