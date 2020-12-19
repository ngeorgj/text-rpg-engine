from game.animations.travel import travel_animation
from game.reference.countries import available_countries


class GeoPositioning:
    COUNTRIES = available_countries

    by_air = [country for country in COUNTRIES if country.has_airport]

    by_sea = [country for country in COUNTRIES if country.has_port]

    @staticmethod
    def make_travel(player, destination):
        travel_animation(player.location, destination)
        player.location = destination
