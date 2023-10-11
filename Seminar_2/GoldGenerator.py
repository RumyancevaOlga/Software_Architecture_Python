from ItemFabric import ItemFabric
from GoldReward import GoldReward


class GoldGenerator(ItemFabric):
    def create_item(self):
        super().create_item()
        print('Create new bag')
        return GoldReward()
