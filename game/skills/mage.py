from game.classes.skill import Skill

# Support Skills
IceArmor   = Skill('Ice Armor',
                   "Hardens your skin with the power of the Ice",
                   500, 5, 11, 3, 3, 3)

# Offensive Skills
Fireball   = Skill('Fireball',
                   'Releases one fireball towards the enemy.',
                   55, 10, 9, 2, 3, 1)

SuperNova  = Skill('Super Nova',
                   'Fire Magic, Invoques a SuperNova.',
                   155, 25, 10, 5, 3, 5)

skills = [
    IceArmor,
    Fireball,
    SuperNova
]