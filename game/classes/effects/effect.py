from game.utils.constants import TEMPORARY
from game.utils.game_functions import game_print


class Effect:
    """
    Effects are activated during the combat, based on their own attributes.

    There are 3 main types of effects.

        Buffs [Healing, Stats]
        Debuffs [Poison, Flame Damage]
        Damage Effects [One time Only or Recurrent Damage]

    """
    # Unchangeable
    is_recurrent = False
    _type = TEMPORARY

    # Changeable
    name = ''
    description = ''
    effect_value = ''
    attribute = ''

    turns = 0
    total_turns = 0

    def __init__(self, properties: dict):
        for arg in properties.items():
            setattr(self, arg[0], arg[1])

    @property
    def specific_options(self):
        return {f'activate {self.name}': self.activate}

    def activate(self):
        """Must be Overwritten"""

    def deactivate(self):
        """Must be Overwritten"""

    def __repr__(self):
        return self.name

