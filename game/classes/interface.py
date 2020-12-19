
class Interface:

    def screen(self):
        print(f'[{self.name} lvl {self.level} ]======================================[GAMENAME]')
        print(f' {self.inventory}                                    Gold {self.inventory.gold}')
        print(f' Experience [2000/10000]                                                       ')
        print(f' Active Effects                                                                ')
        print(f' {[self.active_effects]}                                                       ')
        print(f'[ Actions ]====================================================================')
