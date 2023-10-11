from GoldGenerator import GoldGenerator
from GemGenerator import GemGenerator
from ManaGenerator import ManaGenerator
from DiamondGenerator import DiamondGenerator

from random import choice

lst = [GoldGenerator(), GemGenerator(), ManaGenerator(), DiamondGenerator()]
print(lst)
for i in range(20):
    choice(lst).open_reward()
