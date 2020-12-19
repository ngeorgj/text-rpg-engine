from game.utils.constants import HOTEL


class Location:

    name = ''
    description = ''

    location_type = ''

    actions = {}

class Hotel(Location):
    location_type = HOTEL

    def __init__(self, recepcionist: object, room_cost: int):
        self.recepcionist = recepcionist
        self.room_cost = room_cost

    @property
    def base_actions(self):
        """Actions from the Location"""
        return dict({'spend the night': self.spend_the_night}, **self.recepcionist.actions)

    def specific_actions(self) -> dict:
        """Abstraction, must be replaced with keys and values(not executed functions)"""
        return dict()

    @property
    def actions(self):
        return dict(self.base_actions, **self.specific_actions())

    def spend_the_night(self, character):
        GAME_STATE['DAY'] += 1
