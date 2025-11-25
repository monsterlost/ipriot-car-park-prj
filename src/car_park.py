from sensor import Sensor
from display import Display


class CarPark:
    def __init__(self, location, capacity, plates=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or [] #list - holds references to license plates represented as strings
        self.displays = displays or [] #list - holds references to instances of displays

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays"

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)