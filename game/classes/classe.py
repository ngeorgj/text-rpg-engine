from game.utils.cmd_line_functions import cls
from game.utils.question_functions import question_with_options


class CharacterClass:
    name = ''
    skills = []

    # TYPES OF CLASSES
    PHYSICAL = 'Physical'
    MAGICAL = 'Magical'

    MELEE = 'Melee'
    RANGED = 'Ranged'
    ELEMENTAL = 'Elemental'

    def list_skills(self):
        cls()
        print('List of Skills \n')
        for skill in self.skills:
            print(f' -> {skill} - {skill.description}')
        print()
        return question_with_options('Which one do you want to cast?', [skill.name for skill in self.skills])

    def __repr__(self):
        return self.name


class StrenghtBasedClass(CharacterClass):

    def __init__(self):
        self.build_base = [self.PHYSICAL,
                           self.MELEE]

class AgilityBasedClass(CharacterClass):

    def __init__(self):
        self.build_base = [self.PHYSICAL,
                           self.RANGED,
                           self.MELEE]

class IntelligenceBasedClass(CharacterClass):

    def __init__(self):
        self.build_base = [self.MAGICAL,
                           self.ELEMENTAL,
                           self.RANGED]
