from game.animations.base import intro
from game.config import GAME_OPTIONS, GAME_DESCRIPTION, GAME_NAME, GAME_CHAPTERS
from game.utils.constants import PLAY, CHAPTERS, ABOUT, LORE, HOW_TO_PLAY, QUIT
from game.utils import menu_items
from game.utils.game_functions import end_game
from game.utils.menu_items import game_menu
from game.utils.question_functions import question_with_options, question


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
        for chapter in GAME_CHAPTERS:
            chapter().chapter_loop()
        end_game()


