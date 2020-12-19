from game.utils.cmd_line_functions import cls
from game.utils.game_functions import game_print

from game.utils.shared_functions import text


def question(question, clear_before=False):
    if clear_before:
        cls()
    return input(f' {question}\n -> ')

def question_with_options(question, choices, clear_before=False, silent=False):

    if clear_before:
        cls()

    filtered_choices = []
    is_list = False
    is_dict = False

    if isinstance(choices, dict):
        filtered_choices = [choice[0].lower() for choice in choices.items()]
        is_dict = True

    if isinstance(choices, list):
        filtered_choices = [choice.lower() for choice in choices]
        is_list = True

    def valid_answer():
        cls()
        if 'play' in choices:
            from game.utils.menu_items import game_menu
            game_menu()
        question_with_options(question, choices)

    text(question)

    if not silent:
        for item in filtered_choices:
            print(f' - {item.title()}')

    answer = str(input('\n -> ')).lower()

    if answer not in filtered_choices:
        valid_answer()

    else:
        cls()
        if is_dict:
            try:
                return choices[answer.lower()]
            except:
                return choices[answer.title()]
        if is_list:
            return answer

def press_enter_to_continue():
    input(" > Press 'Enter' to continue.")