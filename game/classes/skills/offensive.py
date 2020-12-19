from game.classes.skills.skill import Skill
from game.utils.constants import OFFENSIVE


class OffensiveSkill(Skill):
    _type = OFFENSIVE

    def cast(self, group_of_enemies):
        damage = self.effect
        for enemy in group_of_enemies:
            enemy.hp -= damage
            print(f'You cast [{self.name}] at {enemy.name} and deals {damage} Damage!')

