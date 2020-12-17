from game.utils.functions import output

class Part:

    def __init__(self, name):
        self.name = f'Part {name}'
        self.segments = [] # functions

    def segment(self):
        pass

    def run(self):
        for segment in self.segments:
            segment()

class Chapter:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.npcs = []
        self.rewards = []
        self.parts = []

    def begin(self):
        output(self.name)
        output(self.description)
        for part in self.parts:
            part.run()
        print(f"End of {self.name}")
