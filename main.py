from item import Item
from player import Player
from game import Game

game = Game()

game.new_game()

rpg_name = 'RPG'

# create some items
# spear = Item('Spear', 5.4, 15, "Long and pointy.")
# dagger = Item('Dagger', 2.0, 17, 'Short and pointy.')
# cloak = Item('Cloak', 3, 20, 'This will keep you warm.')
# sword = Item('Sword', 7, 30, 'Medium length and pointy.')
# shield = Item('Shield', 5, 15, 'This will keep you safe.')


# Character initialization
print(f'Welcome to {rpg_name}!')
print('What is your name? ')
player_name = input('Name: ')
print(f'Welcome {player_name}')
print('What is your class? ')
player_class = input('Class: ')


# create a new player object
player = Player(player_name, 5, 100, player_class)


# Add starter items to player inventory
player.inventory.add_item(dagger)
player.inventory.add_item(cloak)


# game loop
while True:
    command = game.handle_input(player)
    if command == 0:
        break