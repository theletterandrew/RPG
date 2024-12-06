from item import Item
from player import Player

spear = Item('spear', 5.4, 15, "long and pointy.")

print(spear.get_name())
print(spear.get_value())
print(spear.get_description())

player = Player('Andrew', 30, 'Rogue')

print(player.get_name())
print(player.get_player_class())
print(player.inventory.add_item(spear))

print(player.inventory.get_contents())