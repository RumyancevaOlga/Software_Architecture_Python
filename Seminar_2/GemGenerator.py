from ItemFabric import ItemFabric
from GemReward import GemReward


class GemGenerator(ItemFabric):
    def create_item(self):
        super().create_item()
        print('Create new bag')
        return GemReward()
