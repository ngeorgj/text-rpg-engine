"""
// Filename : Instances
// Created by: @ngeorgj

This file holds the base instances for the game, don't change anything!
"""


from game.engine import Engine
from game.cgame import Game

game_engine = Engine()

rpg = Game()
rpg.engine = game_engine
