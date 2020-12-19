from game.classes.effects.buffs import Buff
from game.classes.effects.damage import DamageEffect
from game.classes.skills.offensive import OffensiveSkill
from game.classes.skills.status import StatusSkill
from game.utils.constants import DEFENSIVE, OFFENSIVE


class IceArmor(StatusSkill):

    name = 'Ice Armor'
    description = 'Hardens your skin increasing your armor for 5 turns'

    @property
    def effect(self):
        return Buff({'name': self.name,
                     'description': self.description,
                     'effect_value': 35,
                     'attribute': 'armor',
                     'turns': 5,
                     'total_turns': 5})

    _type               = DEFENSIVE

    mana_cost            = 35

    required_level       = 5
    required_int         = 15
    required_str         = 3
    required_agi         = 3


class Fireball(OffensiveSkill):
    name = 'Fireball'
    description = 'Casts a ball of melting fire into the enemy.'

    @property
    def effect(self):
        return DamageEffect({'name': self.name,
                             'description': self.description,
                             'effect_value': 85,
                             'attribute': 'hp',
                             'turns': 1,
                             'total_turns': 1})

    _type = OFFENSIVE

    mana_cost = 50

    required_level = 1
    required_int = 8
    required_str = 4
    required_agi = 4


# Offensive Skills
SuperNova = OffensiveSkill()

# Compilation
list_of_skills = [
    IceArmor(),
    Fireball,
    SuperNova
]
