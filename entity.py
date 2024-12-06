from inventory import Inventory

class Entity:
    def __init__(self, name, inv_size):
        self.name = name
        self.inv_size = inv_size
        self.inventory = Inventory(self.inv_size)
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_inventory(self):
        return self.inventory