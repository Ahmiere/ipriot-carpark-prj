import unittest
from display import Display
from carpark import CarPark


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display(1, "Welcome to the car park", True, CarPark("123 Example Street", 100))

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)

    def test_update(self):
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")
