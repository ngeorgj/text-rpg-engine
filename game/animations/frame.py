from game.utils.cmd_line_functions import wait, cls
from game.utils.shared_functions import text


def frame(_text, seconds=0.15):
    text(f'\n  {_text}')
    wait(seconds)
    cls()
