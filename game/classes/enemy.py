from game.classes.character import Character


class Enemy(Character):

    name = ''
    title = ''
    race = ''

    classe = ''

    max_hp = 0
    hp = 0

    max_mp = 0
    mp = 0

    strenght = 2
    intelligence = 2
    agility = 2

    inventory = Inventory()
    gold = 0
    weapon: Weapon = object

    skills = []

    is_alive = True

    active_effects: list = []

    actions = {
        OPEN_INVENTORY: inventory.show,
        TRAVEL: Travel.options,
    }

    level = 0
    experience = 0

    in_combat = False
    is_ai = False

    def engage(self, enemy):
        self.in_combat = True
        cbt = Combat(self, enemy)
        cbt.fight()
        self.in_combat = False

    def attack(self, enemy):
        dmg = (self.weapon.damage * self.strenght / 1.4) * random.choice([0.96, 0.97, 0.98, 0.99, 1, 1.01, 1.02])
        multiplier, body_part = get_body_part()
        total_damage = dmg * multiplier
        enemy.hp -= total_damage
        self.refresh_active_effects()

    def refresh_active_effects(self):
        for effect in self.active_effects:
            if effect != PERMANENT:
                if effect.turns_left == effect.total_turns:
                    effect.activate()

            if effect.turns_left == 0:
                self.active_effects.remove(effect)
                print(f'Active Effect : "{effect}" ended this turn.')

            if effect.is_recurrent:
                effect.activate(self)

        for effect in [fx for fx in self.active_effects if fx._type != PERMANENT]:
            effect.turns_left -= 1

    @property
    def available_actions(self):
        if self.is_ai:
            return ATTACK
        lst = self.actions
        if self.in_combat:
            lst.extend(self.weapon.actions)
            for item in self.inventory:
                if GRENADE in item.name:
                    lst.extend(item.actions)
        for item in self.inventory:
            if POTION in item.name and self.hp < self.max_hp:
                lst.extend(item.actions)
        return question_with_options('What will you do?', lst)
