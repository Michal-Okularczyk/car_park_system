import unittest
from pathlib import Path
import json
from car_park import CarPark  # Ensure that CarPark is imported correctly

class TestCarPark(unittest.TestCase):
    CONFIG_FILE = "test_config.json"
    LOG_FILE = Path("test_log.txt")

    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100, log_file=self.LOG_FILE)

    def tearDown(self):
        if Path(self.CONFIG_FILE).exists():
            Path(self.CONFIG_FILE).unlink()
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

    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)
        # Attempt to add an extra car should not change the available bays
        with self.assertRaises(ValueError):
            self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

    def test_register_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.car_park.register("Not a Sensor or Display")

    def test_log_file_created(self):
        self.car_park.add_car("FAKE-001")
        self.assertTrue(self.LOG_FILE.exists())

    def test_car_logged_when_entering(self):
        self.car_park.add_car("NEW-001")
        with self.LOG_FILE.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001 entered", last_line)
        self.assertIn("\n", last_line)

    def test_car_logged_when_exiting(self):
        self.car_park.add_car("NEW-001")
        self.car_park.remove_car("NEW-001")
        with self.LOG_FILE.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001 exited", last_line)
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
