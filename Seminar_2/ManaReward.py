from IGameItem import IGameItem
from random import randint


class ManaReward(IGameItem):
    def open(self):
        super().open()
        quantity = randint(1, 100)
        print(f'Received {quantity} mana')
