class Inventory:
    def __init__(self, size):
        self.contents = {}
        self.size = size
        self.gold = 0
        self.value = 0
    
    def get_contents(self):
        return self.contents

    def add_gold(self, quantity=1):
        self.gold += quantity
        return True
    
    def sub_gold(self, quantity=1):
        if quantity > self.gold:
            return False
        else:
            self.gold -=quantity
            return True
    
    def get_gold(self):
        return self.gold

    def add_item(self, item, quantity=1):
        if len(self.contents) + quantity > self.size:
            return False
        
        if item in self.contents:
            self.contents[item] += quantity
            self.value += item.get_value()
        else:
            self.contents[item] = quantity
            self.value += item.get_value()
        return True

    def remove_item(self, item, quantity=1):
        if item not in self.contents:
            return False
        elif self.contents[item] < quantity:
            return False
        else:
            self.contents[item] -= quantity
            self.value -= item.get_value()
            if self.contents[item] == 0:
                del self.contents[item]
            return True
    
    def get_inventory_size(self):
        return len(self.contents)

    def get_value(self):
        return self.value
    
    def get_item_quantity(self, item):
        if not item in self.contents.keys():
            return None
        else:
            return self.contents[item]