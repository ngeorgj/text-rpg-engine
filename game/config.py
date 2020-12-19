from game.gclasses import Warrior, Paladin, Mage
from game.graces import Human, Elf
from game.reference.countries import available_countries
from game.skills import warrior, mage, paladin
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
    # You can Add/Delete classes.
    # File : game/gclasses.py
    WARRIOR: Warrior(),
    PALADIN: Paladin(),
    MAGE: Mage()
}

SKILLS = {
    WARRIOR : warrior.list_of_skills,
    PALADIN : paladin.list_of_skills,
    MAGE    : mage.list_of_skills,
}

ALLOWED_COUNTRIES = available_countries

GAME_STATE = {
    'YEAR': GAME_STARTING_YEAR,
    'MONTH': 1,
    'DAY': 6,
    'CHAPTERS_LEFT': [chapter for chapter in GAME_CHAPTERS if not chapter.is_complete],
    'CHAPTERS_COMPLETED': [chapter for chapter in GAME_CHAPTERS if chapter.is_complete]
}

