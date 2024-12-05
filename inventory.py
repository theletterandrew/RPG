class Inventory:
    def __init__(self):
        self.contents = {}
    
    def get_contents(self):
        return self.contents
    
    def add_contents(self, item, quantity):
        self.contents