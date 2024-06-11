import unittest
from pathlib import Path
import json
from car_park import CarPark
from display import Display
from sensor import Sensor

class TestCarPark(unittest.TestCase):
    LOG_FILE = Path("test_log.txt")

    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100, log_file=self.LOG_FILE)

    def tearDown(self):
        if Path("config.json").exists():
            Path("config.json").unlink()
        if self.LOG_FILE.exists():
            self.LOG_FILE.unlink()

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, self.LOG_FILE)

    def test_log_file_created(self):
        new_carpark = CarPark("123 Example Street", 100, log_file="new_log.txt")
        self.assertTrue(Path("new_log.txt").exists())

    def test_car_logged_when_entering(self):
        self.car_park.add_car("NEW-001")
        with self.LOG_FILE.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)
        self.assertIn("entered", last_line)
        self.assertIn("\n", last_line)

    def test_car_logged_when_exiting(self):
        self.car_park.add_car("NEW-001")
        self.car_park.remove_car("NEW-001")
        with self.LOG_FILE.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)
        self.assertIn("exited", last_line)
        self.assertIn("\n", last_line)

    def test_write_config(self):
        self.car_park.write_config()
        self.assertTrue(Path("config.json").exists())
        with open("config.json") as f:
            config = json.load(f)
        self.assertEqual(config["location"], self.car_park.location)
        self.assertEqual(config["capacity"], self.car_park.capacity)
        self.assertEqual(config["log_file"], str(self.car_park.log_file))

    def test_from_config(self):
        car_park = CarPark("123 Example Street", 100, log_file=self.LOG_FILE)
        car_park.write_config()
        loaded_car_park = CarPark.from_config("config.json")
        self.assertEqual(loaded_car_park.location, car_park.location)
        self.assertEqual(loaded_car_park.capacity, car_park.capacity)
        self.assertEqual(loaded_car_park.plates, car_park.plates)
        self.assertEqual(loaded_car_park.log_file, car_park.log_file)

if __name__ == "__main__":
    unittest.main()
