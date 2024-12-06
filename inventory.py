class Inventory:
    def __init__(self, size):
        self.contents = {}
        self.size = size
        self.gold = 0
    
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
        else:
            self.contents[item] = quantity
        return True

    def remove_item(self, item, quantity=1):
        if item not in self.contents:
            return False
        elif self.contents[item] < quantity:
            return False
        else:
            self.contents[item] -= quantity
            return True
    
    def get_inventory_size(self):
        return len(self.contents)