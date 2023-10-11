from IGameItem import IGameItem
from random import randint


class GoldReward(IGameItem):
    def open(self):
        super().open()
        quantity = randint(1, 100)
        print(f'Received {quantity} gold')
