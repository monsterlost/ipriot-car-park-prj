class CarPark:
    def __init__(self, location, capacity, plates=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or [] #list - holds references to license plates represented as strings
        self.displays = displays or [] #list - holds references to instances of displays

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays"