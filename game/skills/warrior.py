from game.classes.skills.offensive import OffensiveSkill

# Support Skills
from game.classes.skills.status import StatusSkill

WarShout = StatusSkill()

# Offensive Skills
QuickSlash = OffensiveSkill()
Berzerk = OffensiveSkill()

list_of_skills = [
    WarShout,
    QuickSlash,
    Berzerk
]