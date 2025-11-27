import unittest
from car_park import CarPark
from sensor import EntrySensor
from sensor import ExitSensor

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("a place", 30)
        self.entry_sensor = EntrySensor(1, True, self.car_park)
        self.exit_sensor = ExitSensor(2, True, self.car_park)

    def test_entry_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertEqual(self.entry_sensor.car_park, self.car_park)

    def test_exit_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertEqual(self.exit_sensor.id, 2)
        self.assertEqual(self.exit_sensor.is_active, True)
        self.assertEqual(self.exit_sensor.car_park, self.car_park)

    def test_entry_detect_vehicle(self):
        self.entry_sensor.detect_vehicle()

    def test_exit_detect_vehicle(self):
        self.entry_sensor.detect_vehicle()
        self.exit_sensor.detect_vehicle()

if __name__ == "__main__":
   unittest.main()