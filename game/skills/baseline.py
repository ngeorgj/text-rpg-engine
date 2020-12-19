from game.classes.skill import Skill

# Support Skills
SkillName = Skill('Skill Name',
                  'Skill Description',
                  0, 10, 10, 5, 3, 1)

# Offensive Skills
OffensiveSkill = Skill('Offensive Skill',
                       'Releases one Offense Skill towards the enemy.',
                       55, 10, 9, 2, 3, 1)

skills = [
    SkillName,
]
