import unittest
from sensor import EntrySensor
from carpark import CarPark


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.sensor = EntrySensor(2, True, self.car_park)
        self.sensor.detect_vehicle()

    def test_sensor_initialized_with_all_attributes(self):
        self.assertEqual(self.sensor.id, 2)
        self.assertEqual(self.sensor.is_active, True)
        self.assertEqual(self.sensor.car_park, self.car_park)

    def test_detect_vehicle(self):
        assert len(self.car_park.plates) == 1

        plate = self.car_park.plates[0]
        assert plate.startswith("FAKE-")
        assert len(plate) == 8


if __name__ == '__main__':
    unittest.main()
