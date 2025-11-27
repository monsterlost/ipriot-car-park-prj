from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime


class CarPark:
    def __init__(self, location, capacity, plates=None, displays=None, log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or [] #list - holds references to license plates represented as strings
        self.displays = displays or [] #list - holds references to instances of displays
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays"

    @property
    def available_bays(self):
        if self.capacity < len(self.plates):
            return 0
        else:
            return self.capacity - len(self.plates)

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    def update_displays(self):
        data = {"Available Bays": self.available_bays, "Temperature": 20} #todo: temperature variable
        for display in self.displays:
            display.update(data)

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")