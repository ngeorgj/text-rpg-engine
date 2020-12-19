from game.utils.question_functions import question, question_with_options
from game.utils.constants import OPEN_INVENTORY, TRAVEL
from game.classes.characters.character import Character
from game.classes.geopositioning import GeoPositioning
from game.classes.interface import Interface
from math import floor

class Player(Character, Interface):

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



    @property
    def base_actions(self):
        return {OPEN_INVENTORY: self.inventory.show,
                TRAVEL: GeoPositioning.make_travel}

    def actions(self):
        return dict(self.base_actions, **self.specific_actions)