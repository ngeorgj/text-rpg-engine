from math import floor
from game.classes.character import Character
from game.classes.inventory import Inventory


from game.utils.question_functions import question, question_with_options


class Player(Character):

    def __init__(self):
        from game.config import PLAYABLE_CLASSES, PLAYABLE_RACES
        self.name = question('What is your Hero name?', True)
        self.race = question_with_options('\nWhat is the Race of your Hero?', PLAYABLE_RACES)
        self.classe = question_with_options('What is your Class?', PLAYABLE_CLASSES)

        self.hp = self.classe.hp
        self.mp = self.classe.mp

        self.strenght = self.classe.strenght
        self.intelligence = self.classe.intelligence
        self.agility = self.classe.agility

        self.inventory = Inventory([], 300)

        self.weapon = self.classe.starting_weapon

        self.skills = self.classe.skills

        self.level = self.get_level
        self.experience = 0

    @property
    def get_level(self):
        math = floor(self.experience / 1000)
        if math == 0:
            return 1
        else:
            return math

    def screen(self):
        print(f'[{self.name} lvl {self.level} ]======================================[GAMENAME]')
        print(f' {self.inventory}                                    Gold {self.inventory.gold}')
        print(f' Experience [2000/10000]                                                       ')
        print(f' Active Effects')
        print(f' {[self.active_effects]}')
        print(f'[ Actions ]====================================================================')
