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


class Chapter:
    name = 'name'
    description = 'description'
    npcs = []
    rewards = []

    is_complete = False
    countries_to_add = []

    def __init__(self):
        from game.instances import rpg
        """Working"""
        self.player = rpg.player
        for country in self.countries_to_add:
            from game.config import ALLOWED_COUNTRIES
            ALLOWED_COUNTRIES.append(country)
            print(f"Country {country.name} added to your available Locations.")
        self.play()

    def play(self):
        """Working"""
        print(f'[Chapter - {self.name}]')
        print(f'{self.description}')

        self.story()
        self.ending()
        self.finish()

    def finish(self):
        """Working"""
        self.is_complete = True
        for reward in self.rewards:
            print(f'{reward.amount}x {reward.name} added to your inventory.')
            self.player.inventory.items.append(reward)
