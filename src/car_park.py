import json
from pathlib import Path
from datetime import datetime
from display import Display
from sensor import Sensor

class CarPark:
    def __init__(self, location, capacity, log_file=None):
        self.location = location
        self.capacity = capacity
        self.plates = []
        self.sensors = []
        self.displays = []
        self.available_bays = capacity
        self.log_file = Path(log_file) if log_file else Path("log.txt")
        self.log_file.touch(exist_ok=True)

    def add_car(self, plate):
        if self.available_bays == 0:
            raise ValueError("Car park is full")
        self.plates.append(plate)
        self.available_bays -= 1
        self._log_event(f"{plate} entered at {datetime.now():%Y-%m-%d %H:%M:%S}")

    def remove_car(self, plate):
        if plate not in self.plates:
            raise ValueError(f"Car with plate {plate} not found")
        self.plates.remove(plate)
        self.available_bays += 1
        self._log_event(f"{plate} exited at {datetime.now():%Y-%m-%d %H:%M:%S}")

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
