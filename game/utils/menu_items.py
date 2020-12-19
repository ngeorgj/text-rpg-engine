from game.config import GAME_NAME, GAME_OPTIONS
from game.utils.game_functions import game_print
from game.utils.question_functions import press_enter_to_continue


def about():
    """
    Game Information

    This game .... bla bla bla
    """
    press_enter_to_continue()


def about_chapters(chapters):
    for chapter in chapters:
        game_print(chapter.name)
        game_print(chapter.description)
    press_enter_to_continue()

def about_lore(lore):
    game_print(lore)
    press_enter_to_continue()

def about_htp():
    # To Implement
    press_enter_to_continue()

def game_menu(game_name=GAME_NAME, options=GAME_OPTIONS):
    game_print(f"-------------------------------------------------------  ")
    game_print(f" {game_name}                                             ")
    game_print(f"-------------------------------------------------------  ")
    game_print(f" MENU                                                    ")

    for menu_item in options:
        game_print(f"      > {menu_item}                                  ")

    game_print(f"\n-------------------------------------------------------")

