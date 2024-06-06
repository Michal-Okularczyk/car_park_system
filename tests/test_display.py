import unittest
from display import Display
from car_park import CarPark

class TestDisplay(unittest.TestCase):
    def setUp(self):
        # Create a CarPark object with a default capacity
        self.car_park = CarPark("Example Street", capacity=100)
        # Create a Display object with the CarPark object
        self.display = Display(display_id=1, message="Welcome to the car park", is_on=True, car_park=self.car_park)

    def test_display_initialized_with_all_attributes(self):
        # Test that Display object was initialized with correct attributes
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.display_id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        # Test that update method updates the message attribute
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")

if __name__ == "__main__":
    unittest.main()



