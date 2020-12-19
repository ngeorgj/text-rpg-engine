from game.animations.travel import travel_animation
from game.config import ALLOWED_COUNTRIES
from game.reference.countries import London


class GeoPositioning:

    COUNTRIES = ALLOWED_COUNTRIES

    by_air = []

    by_sea = [

    ]

    @staticmethod
    def make_travel(player, destination):
        travel_animation(player.location, destination)
        player.location = destination
