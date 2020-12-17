import random

class Dice:

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        the_roll = random.randint(1, self.sides)
        print(f'D{self.sides} rolls {the_roll}.')
        return the_roll
