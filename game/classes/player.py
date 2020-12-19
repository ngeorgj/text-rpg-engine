from math import floor
from game.classes.character import Character
from game.classes.inventory import Inventory
from game.reference.playableclasses import PlayableClasses
from game.utils.functions import question


class Player(Character):

    active_effects = []

    def __init__(self):
        self.name            = question('What is your Hero name?')
        self.race            = question('What is the Race of your Hero?')
        self.classe          = PlayableClasses.choose()

        self.hp              = self.classe.hp
        self.mp              = self.classe.mp

        self.strenght        = self.classe.strenght
        self.intelligence    = self.classe.intelligence
        self.agility         = self.classe.agility

        self.inventory       = Inventory([], 300)

        self.weapon          = self.classe.starting_weapon

        self.skills          = self.classe.skills

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