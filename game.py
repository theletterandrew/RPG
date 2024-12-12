from item import Item

class Game:

    def new_game(self):
        # create some items
        self.spear = Item('Spear', 5.4, 15, "Long and pointy.")
        self.dagger = Item('Dagger', 2.0, 17, 'Short and pointy.')
        self.cloak = Item('Cloak', 3, 20, 'This will keep you warm.')
        self.sword = Item('Sword', 7, 30, 'Medium length and pointy.')
        self.shield = Item('Shield', 5, 15, 'This will keep you safe.')


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