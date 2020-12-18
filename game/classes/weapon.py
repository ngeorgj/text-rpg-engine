from game.classes.item import Item


class Weapon(Item):

    def __init__(self, name, description, amount, unit_price, damage, rarity):
        super().__init__(name, description, amount, unit_price)
        self.damage = damage
        self.rarity = rarity

    @property
    def worth(self):
        return self.amount * self.unit_price
