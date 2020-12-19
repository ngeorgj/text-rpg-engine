from game.utils.constants import PERMANENT, TEMPORARY


class Effect:
    is_recurrent = False

    name = ''
    description = ''
    effect = ''
    attribute = ''

    turns = 0
    total_turns = 0

    _type = TEMPORARY

    def __repr__(self):
        return self.name


class Buff(Effect):

    def activate(self):
        setattr(self, self.attribute, getattr(self, self.attribute) + self.effect)

    def deactivate(self):
        setattr(self, self.attribute, getattr(self, self.attribute) - self.effect)


class Debuff(Effect):

    def activate(self):
        setattr(self, self.attribute, getattr(self, self.attribute) - self.effect)

    def deactivate(self):
        setattr(self, self.attribute, getattr(self, self.attribute) + self.effect)


class RecurrentBuff(Buff):
    is_recurrent = True


class RecurrentDebuff(Debuff):
    is_recurrent = True


class MassBuff(Effect):

    def activate(self, group_of_allies):
        for ally in group_of_allies:
            setattr(ally, self.attribute, getattr(ally, self.attribute) + self.effect)

    def deactivate(self, group_of_allies):
        for ally in group_of_allies:
            setattr(ally, self.attribute, getattr(ally, self.attribute) - self.effect)


class MassDebuff(Effect):

    def activate(self, group_of_enemies):
        for ally in group_of_enemies:
            setattr(ally, self.attribute, getattr(ally, self.attribute) - self.effect)

    def deactivate(self, group_of_enemies):
        for ally in group_of_enemies:
            setattr(ally, self.attribute, getattr(ally, self.attribute) + self.effect)


class RecurrentMassBuff(MassBuff):
    is_recurrent = True


class RecurrentMassDebuff(MassBuff):
    is_recurrent = True


class PermanentBuff(Buff):
    _type = PERMANENT
