from math import floor

from game.classes.char_class import classes
from game.classes.character import Character
from game.classes.inventory import Inventory
from game.utils.functions import question


class Player(Character):

    def __init__(self):
        self.name            = question('What is your Hero name?')
        self.race            = question('What is the Race of your Hero?')
        self.char_class      = classes.choose()

        self.hp              = self.char_class.hp
        self.mp              = self.char_class.mp

        self.strenght        = self.char_class.strenght
        self.intelligence    = self.char_class.intelligence
        self.agility         = self.char_class.agility

        self.inventory       = Inventory([], 300)

        self.weapon          = self.char_class.starting_weapon

        self.skills          = self.char_class.skills

        self.level           = self.get_level
        self.experience      = 0

    @property
    def get_level(self):
        return floor(self.experience/1000)

    def screen(self):
        print(f'[{self.name} lvl {self.level} ]======================================[GAMENAME]')
        print(f' {self.inventory}                                    Gold {self.inventory.gold}')
        print(f' Experience [2000/10000]')
        print(f'[ Actions ]====================================================================')