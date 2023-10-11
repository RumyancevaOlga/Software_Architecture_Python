from ItemFabric import ItemFabric
from DiamondReward import DiamondReward


class DiamondGenerator(ItemFabric):
    def create_item(self):
        super().create_item()
        print('Create new bag')
        return DiamondReward()
