import os
import random
import time

from game.config import D020


def output(argument):
    return os.system(argument)

def cls():
    return os.system('cls')

def wait(seconds):
    return time.sleep(seconds)

def get_input(text, choices):
    output(text)
    answer = str(input()).lower()
    if answer not in choices:
        print('please select a valid choice.')
        get_input(text, choices)
    else:
        cls()
        return answer

def press_enter_to_continue():
    input(" > Press 'Enter' to continue.")


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