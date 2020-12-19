from game.classes.pclasses.character_class import CharacterClass


class StrenghtBasedClass(CharacterClass):

    def __init__(self):
        self.build_base = [self.PHYSICAL,
                           self.MELEE]
