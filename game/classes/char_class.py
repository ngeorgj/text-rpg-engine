class CharClass:

    def __init__(self, name, description, int_points, str_points, agi_points):
        self.name = name
        self.description = description
        self.intelligence = int_points
        self.strenght = str_points
        self.agiliyy = agi_points

    def use_skill(self, name):
        pass