from ItemFabric import ItemFabric
from ManaReward import ManaReward


class ManaGenerator(ItemFabric):
    def create_item(self):
        super().create_item()
        print('Create new bag')
        return ManaReward()
