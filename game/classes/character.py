import random

from game.classes.inventory import Inventory
from game.utils.functions import get_body_part


class Character:

    name = ''
    title = ''
    race = ''

    classe = ''

    hp = 0
    mp = 0

    strenght = 2
    intelligence = 2
    agility = 2

    inventory = Inventory()
    gold = 0
    weapon = object()

    skills = []

    is_alive = True

    def attack(self, enemy):
        dmg = (self.weapon.damage * self.strenght / 1.4) * random.choice([0.96, 0.97, 0.98, 0.99, 1, 1.01, 1.02])
        multiplier, body_part = get_body_part()
        total_damage = dmg * multiplier
        enemy.hp -= total_damage
        self.refresh_active_effects()

    def refresh_active_effects(self):
        for effect in self.active_effects:

            if effect.is_recurrent:
                effect.activate(self)

            if effect.turns_left == 0:
                self.active_effects.remove(effect)
                print(f'Active Effect : "{effect}" ended this turn.')


        for effect in [fx for fx in self.active_effects]:
            effect.turns_left -= 1

