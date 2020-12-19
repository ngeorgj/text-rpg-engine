from game.game_classes import Warrior, Paladin, Mage
from game.game_races import Human, Elf
from game.skills import warrior, mage, paladin
from game.reference.countries import London
from game.utils.constants import *
from game.chapters.chapter_one.info import Chapter1

GAME_NAME = 'RPG 1936'
GAME_DESCRIPTION = 'text RPG based in the year of 1936'
GAME_THEME = ''
GAME_CHAPTERS = [Chapter1]
GAME_LORE = ''
GAME_STARTING_YEAR = 1205

GAME_OPTIONS = [PLAY, CHAPTERS, ABOUT, LORE, HOW_TO_PLAY, QUIT]

PLAYABLE_RACES = {
    HUMAN: Human(),
    ELF: Elf()
}

PLAYABLE_CLASSES = {
    WARRIOR: Warrior(),
    PALADIN: Paladin(),
    MAGE: Mage()
}

SKILLS = {
    WARRIOR : warrior.list_of_skills,
    PALADIN : paladin.list_of_skills,
    MAGE    : mage.list_of_skills,
}

ALLOWED_COUNTRIES = [London]

GAME_STATE = {
    'YEAR': GAME_STARTING_YEAR,
    'MONTH': 1,
    'DAY': 6,
    'CHAPTERS_LEFT': [chapter for chapter in GAME_CHAPTERS if not chapter.is_complete],
    'CHAPTERS_COMPLETED': [chapter for chapter in GAME_CHAPTERS if chapter.is_complete]
}

