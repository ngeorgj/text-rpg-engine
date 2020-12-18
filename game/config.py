from game.classes.char_class import classes
from game.utils.constants import *
from game import skills

GAME_NAME = ''
GAME_DESCRIPTION = ''
GAME_THEME = ''
GAME_CHAPTERS = []
GAME_LORE = ''
GAME_OPTIONS = [PLAY, CHAPTERS, ABOUT, LORE, HOW_TO_PLAY, QUIT]

CLASSES = [cls[1] for cls in vars(classes).items()]

SKILLS = {
    WARRIOR: skills.warrior.skills,
    MAGE: skills.mage.skills,
    PALADIN: skills.paladin.skills,
}

