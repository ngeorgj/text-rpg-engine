import random
from game.classes.combat import Combat
from game.classes.inventory import Inventory
from game.classes.weapon import Weapon
from game.utils.constants import PERMANENT
from game.utils.game_functions import get_body_part, game_print
from game.utils.question_functions import question_with_options


class Character:
    """
    The Character base Class

    This class is a baseline for attributes.
    """
    name = ''
    title = ''
    race = ''
    location = ''

    classe = ''

    max_hp = 50
    hp = 50
    max_mp = 20
    mp = 20

    strenght = 2
    intelligence = 2
    agility = 2

    inventory = Inventory()
    gold = 0

    weapon: Weapon = object
    skills = []

    active_effects: list = []

    level = 0
    experience = 0

    is_alive = True
    in_combat = False
    is_ai = False

    def check_is_alive(self):
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            game_print(f'{self.name} is dead.')
            return self.is_alive
        else:
            return True

    def engage(self, enemy):
        self.in_combat = True
        cbt = Combat(self, enemy)
        cbt.fight()
        self.in_combat = False

    def attack(self, enemy):
        damage_multiplier = [0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.01, 1.02]
        dmg = (self.weapon.damage * self.strenght / 1.4) * random.choice(damage_multiplier)
        multiplier, body_part = get_body_part()
        total_damage = dmg * multiplier
        enemy.hp -= total_damage
        enemy.check_is_alive()
        self.refresh_active_effects()

    def refresh_active_effects(self):
        """
        Important Function::refresh_active_effects

        This functions checks all the effects on every combat turn, if it is recurrent, it will "trigger" again.
        """
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
    def base_options(self) -> dict:
        """Overwrite"""

    @property
    def specific_options(self) -> dict:
        """Overwrite"""

    @property
    def available_actions(self):
        """ Complicated """
        dct = dict(self.base_options, **self.specific_options)
        return question_with_options('What will you do?', dct)
