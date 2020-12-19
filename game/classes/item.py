from game.elements import D100
from game.utils.constants import LEGENDARY, EPIC, RARE, UNCOMMON, COMMON


class Item:

    rarities = {
        # Rarity      Multiplier
        COMMON:             1,
        UNCOMMON:         1.3,
        RARE:             1.8,
        EPIC:             2.3,
        LEGENDARY:        4.3
    }

    def get_rarity(self):
        roll = D100.roll()
        if roll == 100:
            return LEGENDARY
        if 97 <= roll <= 99:
            return EPIC
        if 91 <= roll <= 96:
            return RARE
        if 60 <= roll <= 90:
            return UNCOMMON
        else:
            return COMMON

    actions = {}

    def __init__(self, name, description, amount, unit_price):
        self.name = name
        self.description = description
        self.amount = amount
        self.unit_price = unit_price
        self.rarity = self.get_rarity()

    @property
    def worth(self):
        return self.amount * self.unit_price

    def __repr__(self):
        return f'{self.name}[{self.rarity[0]}]'
