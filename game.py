from item import Item
from weapon import Weapon

class Game:

    def new_game(self):
        # create some weapons
        self.spear = Weapon('Spear', 5.4, 15, "Long and pointy.", 10)
        self.dagger = Weapon('Dagger', 2.0, 17, 'Short and pointy.', 7)
        self.sword = Weapon('Sword', 7, 30, 'Medium length and pointy.', 12)
        
        # create some items
        self.cloak = Item('Cloak', 3, 20, 'This will keep you warm.')
        self.torch = Item('Torch', 2, 3, 'This will light the way')


    def handle_input(self, player):
        commands = ['inventory', 'health', 'help', 'quit']
        print('What do you want to do? type help for more info.')
        command = input('> ')
        if command not in commands:
            print("That's not a valid command.")

        elif command == 'help':
            print('These are the valid commands: ')
            print(commands)

        elif command == 'quit':
            return 0

        elif command == 'inventory':
            player.print_inventory()

        elif command == 'health':
            print(player.get_current_health())