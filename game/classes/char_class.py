from game.config import SKILLS
from game.items.weapons import WoodenStaff, RustedSword, SacredHammer

from game.utils.functions import get_input, cls


class CharacterClass:
    name = ''
    description = ''

    intelligence = 0
    strenght = 0
    agility = 0

    skills = SKILLS[name]

    hp = 0
    mp = 0

    starting_weapon = ''

    def use_skill(self):
        cls()
        print('[SKILLS]======================')
        for skill in self.skills:
            print(f' -> {skill} - {skill.description}')
        print()
        return get_input('Which one do you want to cast?', [skill.name for skill in self.skills])

    def __repr__(self):
        return self.name

class Mage(CharacterClass):
    name = 'Mage'
    description = 'An Elder Mage, expert at his magic.'

    intelligence = 15
    strenght = 3
    agility = 3

    hp = 120
    mp = 220

    starting_weapon = WoodenStaff

class Warrior(CharacterClass):
    name = 'Warrior'
    description = 'A Noble Warrior'

    intelligence = 3
    strenght = 15
    agility = 3

    hp = 280
    mp = 40

    starting_weapon = RustedSword

class Paladin(CharacterClass):
    name = 'Paladin'
    description = 'A Sacred Paladin'

    intelligence = 9
    strenght = 8
    agility = 4

    hp = 280
    mp = 40

    starting_weapon = RustedSword

class classes:

    Paladin = Paladin()
    Warrior = Warrior()
    Mage = Mage()

    def choose(self) -> CharacterClass:
        answer = get_input('What is the Class of your Hero?', vars(self).keys)
        return vars(self)[answer]
