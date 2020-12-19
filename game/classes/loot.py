from game.elements import D100
from game.utils.constants import COMMON, UNCOMMON, RARE, EPIC, LEGENDARY


class Loot:

    loot_category = {
        COMMON:             83,
        UNCOMMON:           93,
        RARE:               97,
        EPIC:               99,
        LEGENDARY:         100
    }

    rarities = {
        # Rarity      Multiplier
        COMMON:             1,
        UNCOMMON:         1.3,
        RARE:             1.8,
        EPIC:             2.3,
        LEGENDARY:        4.3
    }

    def get_rarity(self):
        """Returns the rarity and the attr multiplier;"""
        rarity = D100.roll()
        for rar in self.loot_category.items():
            if rar[1] >= rarity:
                return rar[0], self.rarities[rar[0]]
