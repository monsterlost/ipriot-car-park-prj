from abc import ABC, abstractmethod
import random


class Sensor(ABC):
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor {self.id} is {self.is_active}"

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        return "FAKE-" + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        """
        Scans the number plate of a car entering or exiting the car park,
        then displays the information on a Display.

        Parameters
        ----------
        self: either an entry sensor or an exit sensor

        Attributes
        ----------
        plate: the scanned number plate
        update_car_park(EntrySensor): adds the plate to a list, writes the movement to a log,
            then displays that a vehicle has entered the car park
        update_car_park(Exitsensor): removes the plate from the list, writes the movement to a log,
            then displays that a vehicle has exited the car park
        """
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")


class ExitSensor(Sensor):
    def _scan_plate(self):
        return random.choice(self.car_park.plates)

    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")