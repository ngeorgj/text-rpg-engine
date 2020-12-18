class Skill:

    def __init__(self, name, description, effect, mana_cost, req_int, req_str, req_agi, req_lvl):
        self.name = name
        self.description = description

        self.effect = effect
        self.mana_cost = mana_cost

        self.req_level = req_lvl
        self.req_int = req_int
        self.req_str = req_str
        self.req_agi = req_agi

    def cast(self):
        return self.effect

    def __repr__(self):
        return self.name