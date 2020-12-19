"""
// Filename : Chapter
// Created by: @ngeorgj

This File is very important, here lies the parent class for your adventures.

When creating an instance of an Chapter, you need to overwrite some variables:

   - name: str
   - description: str
   - npcs: list
   - rewards: list of Items/Weapons
   - countries_to_add: list of countries (instances)

And you need to overwrite two functions.

   - story
   - ending

The engine will handle everything else!

!IMPORTANT!: Don't forget to add the instances to the game.config file!!
"""
from game.classes import player

class Chapter:

    name = 'name'
    description = 'description'
    npcs = []
    rewards = []

    is_complete = False
    countries_to_add = []

    def __init__(self):
        """Working"""
        self.player = player
        for country in self.countries_to_add:
            from game.config import ALLOWED_COUNTRIES
            ALLOWED_COUNTRIES.append(country)
            print(f"Country {country.name} added to your available Locations.")
        self.chapter_loop()

    def loop_start(self):
        """Working"""
        self.start_line()
        self.story()
        self.finish(self.player)

    def start_line(self):
        """Working"""
        print(f'[Chapter - {self.name}]')

    def finish(self, character):
        """Working"""
        self.is_complete = True
        for reward in self.rewards:
            print(f'{reward.amount}x {reward.name} added to your inventory.')
            character.inventory.items.append(reward)

    def chapter_loop(self):
        """Working"""
        self.loop_start()

        while not self.is_complete:
            self.story()

        self.ending()

    def story(self):
        """Abstraction to be Overwriten"""

    def ending(self):
        """Abstraction to be Overwriten"""
