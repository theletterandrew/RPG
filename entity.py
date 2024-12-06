from inventory import Inventory

class Entity:
    def __init__(self, name, inv_size, health):
        self.name = name
        self.inv_size = inv_size
        self.inventory = Inventory(self.inv_size)
        self.health = health
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_inventory(self):
        return self.inventory

    def print_inventory(self):
        print('-----Inventory-----')
        for item in self.inventory.get_contents():
            print('Name: ' + item.get_name())
            print('Description: ' + item.get_description())
            print('Weight: ' + str(item.get_weight()))
            print('Value: ' + str(item.get_value()))

    def get_health(self):
        return self.health