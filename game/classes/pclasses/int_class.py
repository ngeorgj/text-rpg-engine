from game.classes.pclasses.character_class import CharacterClass


class IntelligenceBasedClass(CharacterClass):

    def __init__(self):
        self.build_base = [self.MAGICAL,
                           self.ELEMENTAL,
                           self.RANGED]
