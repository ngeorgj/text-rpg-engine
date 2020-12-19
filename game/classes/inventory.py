from game.utils.constants import YES, CHOICES_YES_NO
from game.utils.question_functions import question_with_options


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
        answer = question_with_options('Are you sure?', CHOICES_YES_NO)
        if answer == 'yes':
            del self.items[item.name]

    def show(self):
        cls()
        print(f"[Inventory] ===================== Items {len(self.items)}")

    def sell_item(self, item):
        amount = 0
        yes_no = question_with_options('Are you sure?', CHOICES_YES_NO)
        if yes_no == YES:
            if item.amount != 1 and item.amount > 0:
                amount = question_with_options("How many?", ['all', f'You can choose between [1 - {item.amount}]'])
            self.gold += item.worth
            if item.amount == 0:
                del self.items[item]
            print(f'{amount}x of "{item.name}" sold for {item.worth}')
        else:
            print("No items sold.")

    def get_all(self):
        return self.items

    def __repr__(self):
        return f'Inventory [{len(self.items)} Items]'

