from game.classes.geopositioning import GeoPositioning
from game.config import GAME_STATE
from game.utils.constants import HOTEL, AIRPORT
from game.utils.question_functions import question_with_options


class Location:
    name = ''
    description = ''
    location_type = ''

    @property
    def actions(self):
        return dict(self.base_actions, **self.specific_actions())

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

    def spend_the_night(self, character):
        GAME_STATE['DAY'] += 1


class Airport(Location):
    location_type = AIRPORT

    def __init__(self, recepcionist):
        self.recepcionist = recepcionist

    @property
    def base_actions(self):
        """Actions from the Location"""
        return dict({'travel': self.air_travel}, **self.recepcionist.actions)

    def specific_actions(self) -> dict:
        """Abstraction, must be replaced with keys and values(not executed functions)"""
        return dict()

    def air_travel(self, player):
        gp = GeoPositioning()
        answer = question_with_options("Where do you want to go?", gp.by_air, True)
        gp.make_travel(player.location, answer)