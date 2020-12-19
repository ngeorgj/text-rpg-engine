import random

from game.classes.combat import Combat
from game.classes.inventory import Inventory
from game.classes.geopositioning import GeoPositioning
from game.classes.weapon import Weapon
from game.utils.constants import PERMANENT, OPEN_INVENTORY, TRAVEL
from game.utils.game_functions import get_body_part
from game.utils.question_functions import question_with_options


class Character:
    name = ''
    title = ''
    race = ''
    location = ''

    classe = ''

    max_hp = 0
    hp = 0

    max_mp = 0
    mp = 0

    strenght = 2
    intelligence = 2
    agility = 2

    inventory = Inventory()
    gold = 0
    weapon: Weapon = object

    skills = []

    is_alive = True

    active_effects: list = []

    actions = {

    }

    @property
    def base_actions(self):
        return {OPEN_INVENTORY: self.inventory.show,
                TRAVEL: GeoPositioning.make_travel}

    def actions(self):
        return dict(self.base_actions, **self.specific_actions)

    level = 0
    experience = 0

    in_combat = False
    is_ai = False

    def engage(self, enemy):
        self.in_combat = True
        cbt = Combat(self, enemy)
        cbt.fight()
        self.in_combat = False

    def attack(self, enemy):
        # TODO
        dmg = (self.weapon.damage * self.strenght / 1.4) * random.choice([0.96, 0.97, 0.98, 0.99, 1, 1.01, 1.02])
        multiplier, body_part = get_body_part()
        total_damage = dmg * multiplier
        enemy.hp -= total_damage
        self.refresh_active_effects()

    def refresh_active_effects(self):
        for effect in self.active_effects:
            if effect != PERMANENT:
                if effect.turns_left == effect.total_turns:
                    effect.activate()

            if effect.turns_left == 0:
                self.active_effects.remove(effect)
                print(f'Active Effect : "{effect}" ended this turn.')

            if effect.is_recurrent:
                effect.activate(self)

        for effect in [fx for fx in self.active_effects if fx._type != PERMANENT]:
            effect.turns_left -= 1

    @property
    def available_actions(self):
        """ Complicated """
        # TODO : Get the 'actions' property from all the objects inside and compile.
        return question_with_options('What will you do?', lst)
