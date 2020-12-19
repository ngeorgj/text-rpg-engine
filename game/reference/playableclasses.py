from game.classes.classe import CharacterClass
from game.items.weapons import WoodenStaff, RustedSword
from game.utils.functions import get_input


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









class PlayableClasses:

    Paladin = Paladin()
    Warrior = Warrior()
    Mage    = Mage()

    @staticmethod
    def choose() -> object:
        answer = get_input('What is the Class of your Hero?', list(vars(PlayableClasses).keys))
        return vars(PlayableClasses)[answer]
