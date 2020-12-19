from game.classes.skills.skill import Skill
from game.utils.constants import STATUS


class StatusSkill(Skill):
    _type = STATUS

    def cast(self, character):
        character.active_effects.append(self.effect)
        if not self.effect.is_recurrent:
            self.effect.activate()
