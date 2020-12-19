from game.classes.skill import Skill, OffensiveSkill

# Support Skills
WarShout = Skill('War Shout', 'Calls from Forces beyond comprehension.', 45, 0, 2, 3, 3, 1)

# Offensive Skills
QuickSlash = OffensiveSkill('Quick Slash', 'Deals a quick attack to the enemy', 55, 0, 0, 6, 3, 1)
Berzerk = OffensiveSkill('Berzerk', "Goes Berzerk and deals an destructive blow", 255, 0, 1, 5, 3, 3)

skills = [
    WarShout,
    QuickSlash,
    Berzerk
]