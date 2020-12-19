# Parent Class
from game.utils.constants import OFFENSIVE, HEALING, STATUS


class Skill:
    name            = 'name'
    description     = 'description'

    effect          = 'effect'
    mana_cost       = 'mana_cost'

    req_level       = 100
    req_int         = 100
    req_str         = 100
    req_agi         = 100

    available_for   = []  # List of Playable Classes
    _type           = ''

    def __repr__(self):
        return self.name


class OffensiveSkill(Skill):
    _type = OFFENSIVE

    def cast(self, group_of_enemies):
        damage = self.effect
        for enemy in group_of_enemies:
            enemy.hp -= damage
            print(f'You cast [{self.name}] at {enemy.name} and deals {damage} Damage!')


class HealingSkill(Skill):
    _type = HEALING

    def cast(self, group_of_allies: list):
        print(f'You cast {self.name}.')
        for member in group_of_allies:
            member.hp += self.effect
            print(f'{member.name} heals in {self.effect} life points!\n')


class StatusSkill(Skill):
    _type = STATUS

    def __init__(self, name, description, effect, mana_cost, req_int, req_str, req_agi, req_lvl, status_affected):
        super().__init__(name, description, effect, mana_cost, req_int, req_str, req_agi, req_lvl)
        self.status_affected = status_affected

    def cast(self, character):
        character.active_effects.append(self.effect)
        if not self.effect.is_recurrent:
            self.effect.activate()
