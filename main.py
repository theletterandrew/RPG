from item import Item
from player import Player

gold = Item('gold', 1, 'A currency for trading.')

print(gold.get_name())
print(gold.get_value())
print(gold.get_description())

player = Player('Andrew', 'Rogue')

print(player.get_name())
print(player.get_player_class())