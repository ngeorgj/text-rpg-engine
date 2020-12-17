from game.classes.dice import Dice
from game.utils.constants import PLAY, CHAPTERS, ABOUT, LORE, HOW_TO_PLAY, QUIT

GAME_NAME = ''
GAME_DESCRIPTION = ''
GAME_THEME = ''
GAME_CHAPTERS = []
GAME_LORE = ''
GAME_OPTIONS = [PLAY, CHAPTERS, ABOUT, LORE, HOW_TO_PLAY, QUIT]

# Dices
D100 = Dice(20)
D020 = Dice(20)
D010 = Dice(10)
D006 = Dice(6)
D004 = Dice(4)