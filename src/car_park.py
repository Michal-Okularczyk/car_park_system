# car_park.py

from pathlib import Path
from datetime import datetime

class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None, log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = plates if plates is not None else []
        self.sensors = sensors if sensors is not None else []
        self.displays = displays if displays is not None else []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # Create the file if it doesn't exist
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."

    def register(self, component):
        from sensor import Sensor  # Move the import statement here
        from display import Display  # Move the import statement here
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        if plate not in self.plates:
            raise ValueError(f"No car with plate {plate} is parked.")
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    @property
    def available_bays(self):
        return max(0, self.capacity - len(self.plates))

    def update_displays(self):
        from display import Display  # Move the import statement here
        data = {"available_bays": self.available_bays, "temperature": 25}  # Example data
        for display in self.displays:
            display.update(data)

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")
