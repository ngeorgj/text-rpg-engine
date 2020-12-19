import random

class Dice:

    def __init__(self, sides):
        self.sides = sides

    def roll(self, show=False):
        the_roll = random.randint(1, self.sides)
        if show:
            print(f'D{self.sides} rolls {the_roll}.')
        return the_roll
