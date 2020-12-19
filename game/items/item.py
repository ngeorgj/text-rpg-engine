from game.classes.loot import Loot

class Item(Loot):

    actions = {}

    def __init__(self, name, description, amount, unit_price):
        self.name = name
        self.description = description
        self.amount = amount
        self.unit_price = unit_price
        rar, mult = self.get_rarity()
        self.rarity = rar
        self.multiplier = mult

    @property
    def worth(self):
        return self.amount * self.unit_price

    def __repr__(self):
        return f'{self.name}[{self.rarity[0]}]'
