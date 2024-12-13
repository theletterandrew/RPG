from item import Item
from weapon import Weapon
from player import Player
from npc import Npc


# Create some items---------------------
# spear = Item('Spear', 5.4, 15, "Long and pointy.")
dagger = Weapon('Dagger', 2.0, 17, 'Short and pointy.', 10)
cloak = Item('Cloak', 3, 20, 'This will keep you warm.')
# sword = Item('Sword', 7, 30, 'Medium length and pointy.')
# shield = Item('Shield', 5, 15, 'This will keep you safe.')
potion = Item('Health Potion', 1, 15, 'Drink this for more health.')


# print(spear.get_name())
# print(spear.get_value())
# print(spear.get_description())


# Create a new player object------------
player = Player('Andrew', 5, 100, 'Rogue')
# print(player.get_health())
# print(player.get_name())
# print(player.get_player_class())


# Add items to player inventory---------
# print(player.inventory.add_item(spear))
print(player.inventory.add_item(dagger))
print(player.inventory.add_item(cloak))
# print(player.inventory.add_item(sword))
# print(player.inventory.add_item(shield))


print(player.inventory.add_gold(50))
print(player.inventory.get_gold())

# returns a dictionary of objects in inventory
print(player.inventory.get_contents())

player.print_inventory()
print(player.inventory.get_value())

# Delete item from inventory-------
print(player.inventory.remove_item(cloak))
player.print_inventory()

# Check item quantity
print(player.inventory.get_item_quantity(dagger))

# Check player health and if alive
print(player.get_current_health())
print(player.check_alive())

# Subtract player health and check current health
player.sub_health(25)
print(player.get_current_health())

# Create a new NPC
hagdar = Npc('Hagdar', 5, 50)
print(hagdar.check_alive())

print(player.get_max_hit())
player.update_max_hit()
print(player.get_max_hit())
print("Attack: " + str(player.attack()))