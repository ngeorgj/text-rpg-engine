"""
** Attention: Do not change any values in this file!

// Filename : Engine
// Created by: @ngeorgj

This file organizes basically everything.

It serves as a base for the first menu in the game.
"""

from game.animations.intro import intro
from game.config import GAME_OPTIONS, GAME_DESCRIPTION, GAME_NAME, GAME_CHAPTERS
from game.utils.constants import PLAY, CHAPTERS, ABOUT, LORE, HOW_TO_PLAY, QUIT
from game.utils import menu_items
from game.utils.game_functions import end_game
from game.utils.menu_items import game_menu
from game.utils.question_functions import question_with_options


class Engine:

    def select_from_menu(self, option, game):
        option = option.lower()
        if option == PLAY:
            self.play(game)
        elif option == ABOUT:
            menu_items.about()
        elif option == CHAPTERS:
            menu_items.about_chapters()
        elif option == LORE:
            menu_items.about_lore()
        elif option == HOW_TO_PLAY:
            menu_items.about_htp()
        elif option == QUIT:
            quit()
        else:
            game_menu(GAME_NAME, GAME_OPTIONS)

    def run(self, game):
        intro(GAME_NAME, GAME_DESCRIPTION)
        game_menu()
        output = question_with_options('Type your answer below', GAME_OPTIONS, False, True)
        self.select_from_menu(output, game)

    def play(self, game):
        game.create_character()
        [chapter().loop_start() for chapter in GAME_CHAPTERS if not chapter.is_complete]
        end_game()


