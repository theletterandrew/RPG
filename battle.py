import time
from player import Player

class Battle:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent


    def battle_loop(self):
        while self.player.check_alive() and self.opponent.check_alive():

            player_hit = self.player.attack()
            print(f'You deal {player_hit} damage.')
            self.opponent.sub_health(player_hit)
            print('Opponent health: ' + str(self.opponent.get_current_health()))
            time.sleep(1)
            if self.opponent.check_alive():
                opponent_hit = self.opponent.attack()
                print(f'Opponent deals {opponent_hit} damage to you.')
                self.player.sub_health(opponent_hit)
                print('Your health: ' + str(self.player.get_current_health()))
                time.sleep(1)