from game.classes.skill import Skill

# Support Skills
LesserHeal = Skill('Lesser Heal', 'Restores a small amount of health', 20, 12, 5, 1, 1, 3)
Heal       = Skill('Heal', 'Restores some Health', 35, 18, 8, 2, 3, 5)

# Offensive Skills
HammerOfGod = Skill('Hammer of God', 'Cast the Hammer of God onto your enemy', 255, 15, 8, 3, 3, 2)

skills = [
    LesserHeal,
    Heal,
    HammerOfGod
]