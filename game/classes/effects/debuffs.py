from game.classes.effects.buffs import MassBuff
from game.classes.effects.effect import Effect


class Debuff(Effect):

    def activate(self):
        self.on_cast()
        setattr(self, self.attribute, getattr(self, self.attribute) - self.effect_value)

    def deactivate(self):
        setattr(self, self.attribute, getattr(self, self.attribute) + self.effect_value)

class RecurrentDebuff(Debuff):
    is_recurrent = True

class MassDebuff(Effect):

    def activate(self, group_of_enemies):
        self.on_cast()
        for ally in group_of_enemies:
            setattr(ally, self.attribute, getattr(ally, self.attribute) - self.effect_value)

    def deactivate(self, group_of_enemies):
        for ally in group_of_enemies:
            setattr(ally, self.attribute, getattr(ally, self.attribute) + self.effect_value)

class RecurrentMassDebuff(MassBuff):
    is_recurrent = True

