from entity import Entity

class Player(Entity):
    def __init__(self, name, inv_size, max_health, player_class):
        super().__init__(name, inv_size, max_health)
        self.player_class = player_class
    
    def get_player_class(self):
        return self.player_class