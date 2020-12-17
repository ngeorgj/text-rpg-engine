from game.utils.functions import press_enter_to_continue

def about():
    """
    Game Information

    This game .... bla bla bla
    """
    press_enter_to_continue()


def about_chapters(chapters):
    for chapter in chapters:
        print(chapter.name)
        print(chapter.description)
    press_enter_to_continue()

def about_lore(lore):
    print(lore)
    press_enter_to_continue()

def about_htp():
    # To Implement
    press_enter_to_continue()

def game_menu(game_name, options):
    print(f"-------------------------------------------------------  ")
    print(f" {game_name}                                             ")
    print(f"-------------------------------------------------------  ")
    print(f" MENU                                                    ")

    for menu_item in options:
        print(f"      > {menu_item}                                  ")

    print(f"\n-------------------------------------------------------")
