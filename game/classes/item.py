class Item:

    rarities = {
        # Rarity      Multiplier
        'common':             1,
        'uncommon':         1.3,
        'rare':             1.8,
        'epic':             2.3,
        'legendary':        4.3
    }

    def __init__(self, name, description, amount, unit_price):
        self.name = name
        self.description = description
        self.amount = amount
        self.unit_price = unit_price

    @property
    def worth(self):
        return self.amount * self.unit_price
