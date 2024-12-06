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

# returns a dictionary of objects in inventory
print(player.inventory.get_contents())

player.print_inventory()
print(player.inventory.get_value())

# Delete item from inventory-------
print(player.inventory.remove_item(cloak))
player.print_inventory()

# Add an extra dagger to see if it shows up
print(player.inventory.add_item(dagger))

# Check item quantity
print(player.inventory.get_item_quantity(dagger))

