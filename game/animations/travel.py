from game.animations.frame import frame
from game.utils.game_functions import game_print
from game.utils.shared_functions import game_says


def travel_animation(position, destination):
    way = '                                  '
    counter = 0
    while True:
        way = way.replace(' ', '-', counter)
        game_print(f'\n Traveling from {position} to {destination}')
        frame(f'[{position}] ' + way + f' [{destination}]', 1)
        counter += 1
        if counter >= len(way) / 3.2:
            break
    game_says(f'You arrived at the destination ({destination})')