from item import Item

class Weapon(Item):
    def __init__(self, name, weight, value, description, max_hit):
        super().__init__(name, weight, value, description)
        self.max_hit = max_hit