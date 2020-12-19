"""
// Filename : GClasses
// Created by: @ngeorgj

Classes can be created using the parent classes from game/classes/classe.

    - Some pre-made classes are:
      -> IntelligenceBasedClass,
      -> StrenghtBasedClass,
      -> AgilityBasedClass

Use these classes as Parent Class for your Class.
Use the classes below as a baseline.
"""

from game.classes.classe import IntelligenceBasedClass, StrenghtBasedClass
from game.items.weapons import RustedSword, WoodenStaff

class Mage(IntelligenceBasedClass):
    name = 'Mage'
    description = 'An Elder Mage, expert at his magic.'

    intelligence = 15
    strenght = 3
    agility = 3

    hp = 120
    mp = 220

    starting_weapon = WoodenStaff


class Warrior(StrenghtBasedClass):
    name = 'Warrior'
    description = 'A Noble Warrior'

    intelligence = 3
    strenght = 15
    agility = 3

    hp = 280
    mp = 40

    starting_weapon = RustedSword


class Paladin(IntelligenceBasedClass):
    name = 'Paladin'
    description = 'A Sacred Paladin'

    intelligence = 9
    strenght = 8
    agility = 4

    hp = 280
    mp = 40

    starting_weapon = RustedSword

