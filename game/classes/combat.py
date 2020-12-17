class Combat:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.fight()
        self.stats = {self.player.name: '',
                      self.enemy.name: ''}
        self.fight()

    def fight(self):
        while self.player.is_alive() and self.enemy.is_alive():
            self.player.attack(self.enemy)
            self.enemy.attack(self.player)
        show = input('\n Show Stats? [y/n] \n -> ')
        if show:
            self.show_stats()

    def show_stats(self):
        player_damage = self.stats[self.player.name]['damage']
        enemy_damage = self.stats[self.enemy.name]['damage']
        print(player_damage, enemy_damage)