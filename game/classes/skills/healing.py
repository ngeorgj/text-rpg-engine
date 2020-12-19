from game.classes.skills.skill import Skill
from game.utils.constants import HEALING


class HealingSkill(Skill):
    _type = HEALING

    def cast(self, group_of_allies: list):
        print(f'You cast {self.name}.')
        for member in group_of_allies:
            member.hp += self.effect
            print(f'{member.name} heals in {self.effect} life points!\n')

