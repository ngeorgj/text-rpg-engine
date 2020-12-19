from game.classes.effects.effect import Effect
from game.utils.constants import PERMANENT


class Buff(Effect):

    def activate(self):
        setattr(self, self.attribute, getattr(self, self.attribute) + self.effect_value)

    def deactivate(self):
        setattr(self, self.attribute, getattr(self, self.attribute) - self.effect_value)


class RecurrentBuff(Buff):
    is_recurrent = True


class MassBuff(Effect):

    def activate(self, group_of_allies):
        for ally in group_of_allies:
            setattr(ally, self.attribute, getattr(ally, self.attribute) + self.effect_value)

    def deactivate(self, group_of_allies):
        for ally in group_of_allies:
            setattr(ally, self.attribute, getattr(ally, self.attribute) - self.effect_value)


class RecurrentMassBuff(MassBuff):
    is_recurrent = True


class PermanentBuff(Buff):
    _type = PERMANENT
