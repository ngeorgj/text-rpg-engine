from game.classes.pclasses.character_class import CharacterClass


class AgilityBasedClass(CharacterClass):

    def __init__(self):
        self.build_base = [self.PHYSICAL,
                           self.RANGED,
                           self.MELEE]