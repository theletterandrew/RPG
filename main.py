from item import Item
from player import Player
from game import Game

game = Game()

game.new_game()

rpg_name = 'RPG'

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
player.inventory.add_item(game.dagger)
player.inventory.add_item(game.cloak)


# game loop
while True:
    command = game.handle_input(player)
    if command == 0:
        break