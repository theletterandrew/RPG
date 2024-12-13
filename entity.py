from inventory import Inventory
from weapon import Weapon
import random


class Entity:
    def __init__(self, name, inv_size, max_health):
        self.name = name
        self.inv_size = inv_size
        self.inventory = Inventory(self.inv_size)
        self.max_health = max_health
        self.current_health = self.max_health
        self.alive = True
        self.max_hit = 5
    

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
            if isinstance(item, Weapon):
                print('Max Hit: ' + str(item.get_max_hit()))
            print('--------------------')


    def get_max_health(self):
        return self.max_health


    def get_current_health(self):
        return self.current_health
    

    def check_alive(self):
        return self.alive


    def sub_health(self, amount):
        if amount > self.get_current_health():
            self.current_health = 0
            self.alive = False
        else:
            self.current_health -= amount


    def add_health(self, amount):
        if amount + self.get_current_health() >= self.get_max_health():
            self.current_health = self.max_health
        else:
            self.current_health += amount


    def get_max_hit(self):
        self.update_max_hit()
        return self.max_hit


    def update_max_hit(self):
        self.max_hit = self.inventory.get_weapon().get_max_hit()

    
    def attack(self):
        return random.randint(0, self.get_max_hit())