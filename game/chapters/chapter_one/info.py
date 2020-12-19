from game.classes.chapter import Chapter
from .npcs import mary_claire, alfred_santiago
from ...utils.shared_functions import text


class Chapter1(Chapter):
    name = 'The Rebelion'
    description = 'After 23 years of servitude...'

    npcs = [mary_claire,
            alfred_santiago]

    def story(self):
        from ...config import GAME_STATE
        text(f"The year was {GAME_STATE['YEAR']}, you walk towards the city of Ashalá.")
        text("What can you expect of this wasteland?")
















