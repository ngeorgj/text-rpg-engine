from game.elements import D020
import random

def game_print(content):
    print(f' {content}')

def get_body_part():
    """
    :return: damage multiplier, body part
    """
    body = {
        'head': 2,
        'torso': 1.5,
        'left-arm': 1.1,
        'right-arm': 1.1,
        'right-leg': 0.95,
        'left-leg': 0.95,
        'missed': 0
    }
    roll = D020.roll()
    if roll == 20:
        return body['head'], 'head'
    elif roll >= 16 or roll <= 19:
        return body['torso'], 'torso'
    elif roll >= 11 or roll <= 15:
        arms = ['left', 'right']
        arm = '-arm'
        composed = f'{random.choice(arms)}{arm}'
        return body[composed], composed
    elif roll >= 4 or roll <= 14:
        legs = ['left', 'right']
        leg = '-leg'
        composed = f'{random.choice(legs)}{leg}'
        return body[composed], composed
    else:
        return body['missed'], 'missed'

def end_game():
    from game.utils.question_functions import press_enter_to_continue
    print("Thanks for Playing!")
    press_enter_to_continue()

