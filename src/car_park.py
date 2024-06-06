import json
from pathlib import Path

class CarPark:
    def __init__(self, location, capacity, log_file=None):
        self.location = location
        self.capacity = capacity
        self.plates = []
        self.sensors = []
        self.displays = []
        self.available_bays = capacity
        self.log_file = log_file

    def add_car(self, plate):
        if self.available_bays == 0:
            return
        self.plates.append(plate)
        self.available_bays -= 1
        self._log_event(f"{plate} entered")

    def remove_car(self, plate):
        if plate not in self.plates:
            raise ValueError(f"Car with plate {plate} not found")
        self.plates.remove(plate)
        self.available_bays += 1
        self._log_event(f"{plate} exited")

    def register(self, item):
        if isinstance(item, Sensor):
            self.sensors.append(item)
        elif isinstance(item, Display):
            self.displays.append(item)
        else:
            raise TypeError("item must be a Sensor or Display")

    def _log_event(self, event):
        if self.log_file:
            with self.log_file.open('a') as f:
                f.write(event + '\n')

    def write_config(self):
        with open("config.json", "w") as f:
            json.dump({
                "location": self.location,
                "capacity": self.capacity,
                "log_file": str(self.log_file)
            }, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=Path(config["log_file"]))

class Sensor:
    def __init__(self, sensor_id, is_active, car_park):
        self.sensor_id = sensor_id
        self.is_active = is_active
        self.car_park = car_park

    # Define other methods as needed

class EntrySensor(Sensor):
    def car_arrived(self, plate):
        if self.is_active:
            self.car_park.add_car(plate)
            print(f"Incoming vehicle detected. Plate: {plate}")


class ExitSensor(Sensor):
    def car_departed(self, plate):
        if self.is_active:
            self.car_park.remove_car(plate)
            print(f"Outgoing vehicle detected. Plate: {plate}")


class Display:
    def __init__(self, display_id, message="", is_on=False, car_park=None):
        self.display_id = display_id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def update_display(self, message):
        if self.is_on:
            self.message = message
            print(f"Display {self.display_id}: {self.message}")

