from game.classes.skills.skill import OffensiveSkill, StatusSkill


# Support Skills
class IceArmor(StatusSkill):
    name = 'Ice Armor'
    description = 'Hardens your skin increasing your armor for 5 turns'


# Offensive Skills
Fireball   = OffensiveSkill()
SuperNova  = OffensiveSkill()

# Compilation
list_of_skills = [
    IceArmor,
    Fireball,
    SuperNova
]