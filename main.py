from item import Item
from player import Player


# Create some items---------------------
spear = Item('Spear', 5.4, 15, "Long and pointy.")
dagger = Item('Dagger', 2.0, 17, 'Short and pointy.')
cloak = Item('Cloak', 3, 20, 'This will keep you warm.')
sword = Item('Sword', 7, 30, 'Medium length and pointy.')
shield = Item('Shield', 5, 15, 'This will keep you safe.')
potion = Item('Health Potion', 1, 15, 'Drink this for more health.')


# print(spear.get_name())
# print(spear.get_value())
# print(spear.get_description())


# Create a new player object------------
player = Player('Andrew', 5, 'Rogue')
# print(player.get_name())
# print(player.get_player_class())

# Add items to player inventory---------
print(player.inventory.add_item(spear))
print(player.inventory.add_item(dagger))
print(player.inventory.add_item(cloak))
print(player.inventory.add_item(sword))
print(player.inventory.add_item(shield))

# set inventory size to 5 to see if you can still add items once full
print(player.inventory.add_item(potion))
print(player.inventory.get_inventory_size())

print(player.inventory.add_gold(50))
print(player.inventory.get_gold())

# print(player.inventory.get_contents())
# returns a dictionary of objects in inventory


# iterate through dictionary of objects in inventory and print name of item, description, and item weight
for item in player.inventory.get_contents():
    print(item.get_name(), item.get_description(), item.get_weight())