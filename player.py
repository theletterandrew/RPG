from entity import Entity

class Player(Entity):
    def __init__(self, name, player_class):
        super().__init__(name)
        self.player_class = player_class
    

    def get_player_class(self):
        return self.get_player_class