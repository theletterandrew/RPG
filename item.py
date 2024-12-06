class Item:
    def __init__(self, name, weight, value, description):
        self.name = name
        self.weight = weight
        self.value = value
        self.description = description

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value

    def get_description(self):
        return self.description