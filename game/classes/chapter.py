from game.classes import player


class Part:

    def __init__(self, name):
        self.name = f'Part {name}'
        self.segments = []  # functions

    def segment(self):
        pass

    def run(self):
        for segment in self.segments:
            segment()


class Chapter:

    name = 'name'
    description = 'description'
    npcs = []
    rewards = []
    parts = []

    is_complete = False
    countries_to_add = []

    def __init__(self):
        self.player = player
        for country in self.countries_to_add:
            from game.config import ALLOWED_COUNTRIES
            ALLOWED_COUNTRIES.append(country)
            print(f"Country {country.name} added to your available Locations.")
        self.chapter_loop()

    def loop_start(self):
        self.start_line()
        self.story()
        self.finish(self.player)

    def start_line(self):
        print(f'[Chapter - {self.name}]')

    def finish(self, character):
        self.is_complete = True
        for reward in self.rewards:
            print(f'{reward.amount}x {reward.name} added to your inventory.')
            character.inventory.items.append(reward)

    def chapter_loop(self):
        self.loop_start()

        while not self.is_complete:
            self.story()

        self.ending()

    def story(self):
        """Abstraction to be Overwriten"""

    def ending(self):
        """Abstraction to be Overwriten"""
