from game.classes.player import Player


class Game:

    engine = object
    _player = object

    def create_character(self):
        player = Player()
        self._player = player
        return player

    @property
    def player(self):
        return self._player

    def run(self):
        self.engine.run(self)