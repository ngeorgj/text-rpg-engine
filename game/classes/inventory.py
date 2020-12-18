from game.utils.functions import get_input, cls


class Inventory:

    def __init__(self, items=False, gold=False):
        if items:
            self.items = items
            self.gold = gold

    def add(self, item):
        self.items[item.name] = item

    def remove(self, item):
        for item in self.items:
            print(f'{item.name} x {item.amount}')
        answer = get_input('Are you sure?', ['yes', 'no'])
        if answer == 'yes':
            del self.items[item.name]

    def show(self):
        cls()
        print(f"[Inventory] ===================== Items {len(self.items)}")

    def sell_item(self, item):
        answer = get_input('Are you sure?', ['yes', 'no'])
        if answer == 'yes':
            del self.items[item]
        self.gold += item.worth
        print(f'Item sold for {item.worth}')

    def get_all(self):
        return self.items

    def __repr__(self):
        return f'Inventory [{len(self.items)} Items]'

