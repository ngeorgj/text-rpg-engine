"""
// Filename : GRaces
// Created by: @ngeorgj

Races can be created using the parent class Race.

Use this class as Parent Class for your Race Class.
Use the classes below as a baseline.

Feel free to add more variables and redesign it.
"""

from game.classes.race import Race


class Human(Race):
    name = "Human"
    lore = "Bipeds with depression."


class Elf(Race):
    name = 'Elf'
    lore = "They live hidden in the woods."
