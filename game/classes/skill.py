# Parent Class
class Skill:

    def __init__(self, name, description, effect, mana_cost, req_int, req_str, req_agi, req_lvl):
        self.name = name
        self.description = description

        self.effect = effect
        self.mana_cost = mana_cost

        self.req_level = req_lvl
        self.req_int = req_int
        self.req_str = req_str
        self.req_agi = req_agi

    def __repr__(self):
        return self.name

class OffensiveSkill(Skill):

    def cast(self, group_of_enemies):
        damage = self.effect
        for enemy in group_of_enemies:
            enemy.hp -= damage
            print(f'You cast [{self.name}] at {enemy.name} and deals {damage} Damage!')


class HealingSkill(Skill):

    def cast(self, group_of_allies: list):
        print(f'You cast {self.name}.')
        for member in group_of_allies:
            member.hp += self.effect
            print(f'{member.name} heals in {self.effect} life points!')


class StatusSkill(Skill):

    def __init__(self,name, description, effect, mana_cost, req_int, req_str, req_agi, req_lvl, status_affected):
        super().__init__(name, description, effect, mana_cost, req_int, req_str, req_agi, req_lvl)
        self.status_affected = status_affected

    def cast(self,):
        attr = getattr(self, self.status_affected)
