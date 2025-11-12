import unittest
from carpark import CarPark

class TestCarPark(unittest.TestCase):
      def setUp(self):
         self.carpark = CarPark("123 Example Street", 100)

      def test_car_park_initialized_with_all_attributes(self):
         self.assertIsInstance(self.carpark, CarPark)
         self.assertEqual(self.carpark.location, "123 Example Street")
         self.assertEqual(self.carpark.capacity, 100)
         self.assertEqual(self.carpark.plates, [])
         self.assertEqual(self.carpark.displays, [])
         self.assertEqual(self.carpark.available_bays, 100)

      def test_add_car(self):
         self.carpark.add_car("FAKE-001")
         self.assertEqual(self.carpark.plates, ["FAKE-001"])
         self.assertEqual(self.carpark.available_bays, 99)

      def test_remove_car(self):
         self.carpark.add_car("FAKE-001")
         self.carpark.remove_car("FAKE-001")
         self.assertEqual(self.carpark.plates, [])
         self.assertEqual(self.carpark.available_bays, 100)

      def test_overfill_the_car_park(self):
         for i in range(100):
            self.carpark.add_car(f"FAKE-{i}")
         self.assertEqual(self.carpark.available_bays, 0)
         self.carpark.add_car("FAKE-100")
         # Overfilling the car park should not change the number of available bays
         self.assertEqual(self.carpark.available_bays, 0)

         # Removing a car from an overfilled car park should not change the number of available bays
         self.carpark.remove_car("FAKE-100")
         self.assertEqual(self.carpark.available_bays, 0)

      def test_removing_a_car_that_does_not_exist(self):
         with self.assertRaises(ValueError):
            self.carpark.remove_car("NO-1")


if __name__ == "__main__":
   unittest.main()