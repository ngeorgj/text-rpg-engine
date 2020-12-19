from game.classes.effects.buffs import Effect

class DamageEffect(Effect):
    """not recurrent"""
    def activate(self, enemy):
        self.on_cast()
        enemy.hp -= self.effect_value


class RecurrentDamageEffect(DamageEffect):
    is_recurrent = True

