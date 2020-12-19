class Skill:
    """Parent class for Skill Abstractions"""
    name                 = 'name'
    description          = 'description'

    effect               = object
    mana_cost            = 50

    required_level       = 100
    required_int         = 100
    required_str         = 100
    required_agi         = 100

    available_for        = []  # List of Playable Classes
    _type                = ''

    def __repr__(self):
        return self.name




