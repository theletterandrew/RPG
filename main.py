from item import Item
from player import Player
from npc import Npc
from game import Game
from battle import Battle

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


# create a new Player object
player = Player(player_name, 5, 100, player_class)

# create an Npc opponent
hagdar = Npc('Hagdar', 5, 75)


# Add starter items to player inventory
player.inventory.add_item(game.dagger)
player.inventory.add_item(game.cloak)
player.inventory.add_item(game.torch)


# game loop
while True:
    command = game.handle_input(player)
    if command == 'quit':
        break
    elif command == 'fight':
        battle = Battle(player, hagdar)
        battle.battle_loop()