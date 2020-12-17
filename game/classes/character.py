import random

from game.classes.inventory import Inventory
from game.utils.functions import get_body_part


class Character:

    name = ''
    title = ''
    race = ''

    char_class = ''

    hp = 0
    mp = 0

    strenght = 5
    intelligence = 4
    agility = 5

    inventory = Inventory()
    gold = 0
    weapon = object()

    skills = []

    def attack(self, enemy):
        dmg = (self.weapon.damage * self.strenght / 1.4) * random.choice([0.96, 0.97, 0.98, 0.99, 1, 1.01, 1.02])
        multiplier, body_part = get_body_part()
        total_damage = dmg * multiplier
        enemy.hp -= total_damage
        print(f"{self.name} {self.weapon.on_attack_fx} at {enemy}'s {body_part} dealing {total_damage} damage.")

