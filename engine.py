from game.animations.base import intro
from game.config import GAME_OPTIONS, GAME_DESCRIPTION, GAME_NAME, GAME_CHAPTERS
from game.utils.constants import PLAY, CHAPTERS, ABOUT, LORE, HOW_TO_PLAY, QUIT
from game.utils.functions import get_input
from game.utils import menu_items
from game.utils.menu_items import game_menu

class Engine:

    def select_from_menu(self, option):
        option = option.lower()
        if option == PLAY:
            self.play()
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
        game_menu(GAME_OPTIONS)

    def run(self):
        intro(GAME_NAME, GAME_DESCRIPTION)
        game_menu(GAME_NAME, GAME_OPTIONS)
        answer = get_input('Answer below:', GAME_OPTIONS)
        self.select_from_menu(answer)

    def end_game(self):
        print("Thanks for Playing!")
        pass

    def play(self):
        for chapter in GAME_CHAPTERS:
            chapter.begin()
        self.end_game()

