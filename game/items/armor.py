from game.items.item import Item

class Armor(Item):
    equip_at = ''
    armor = 0

    def __init__(self, name, description, amount, unit_price, equip_at, armor):
        super().__init__(name, description, amount, unit_price)
        self.armor = armor * self.multiplier
        self.equip_at = equip_at

