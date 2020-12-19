from game.classes.character import Character


class NPC(Character):

    def __init__(self, dictionary):
        for item in dictionary.items():
            setattr(self, item[0], item[1])