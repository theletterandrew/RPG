from inventory import Inventory

class Entity:
    def __init__(self, name, inventory):
        self.name = name
        if inventory is not None:
            self.inventory = inventory
        else:
            self.inventory = Inventory()
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_inventory(self):
        return self.inventory