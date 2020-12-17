from game.utils.functions import cls, wait, output

def frame(text, seconds=0.15):
    output(text)
    wait(seconds)
    cls()

def intro(game_name, game_description):
    frame(game_name, 1)
    frame(game_description, 1)
    # needs completion

