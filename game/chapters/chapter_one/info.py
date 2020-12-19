from game.classes.chapter import Chapter
from .npcs import mary_claire, alfred_santiago

name = 'The Rebelion'
description = 'After 23 years of servitude...'

class Chapter1(Chapter):
    name = name
    description = description

    npcs = [mary_claire,
            alfred_santiago]

















