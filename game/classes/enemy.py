import random
from game.classes.character import Character
from game.utils.constants import TRAVEL, ATTACK, CAST_SPELL, COMMON, UNCOMMON, RARE, EPIC, LEGENDARY


class Enemy(Character):

    def __init__(self, name, race, classe, level, max_hp, max_mp):
        self.name = name
        self.race = race
        self.classe = classe
        self.level = level
        self.hp = max_hp
        self.max_hp = max_hp
        self.mp = max_mp
        self.max_mp = max_mp
        self.intelligence = self.random_stats
        self.agility = self.random_stats
        self.strenght = self.random_stats
        self.weapon = self.get_random_weapon()
        self.skills = self.classe.skills

    active_effects: list = []

    in_combat = False
    is_ai = True
    is_alive = True

    @property
    def available_actions(self):
        actions = {
            ATTACK: self.attack,
            CAST_SPELL: self.skills
        }
        check = random.randint(1, 100)
        if check > 80:
            return actions[CAST_SPELL]
        else:
            return actions[ATTACK]

    @property
    def random_stats(self):
        return random.randint(1, 20)

    def get_random_weapon(self):
        pass
