# sensor.py

class Sensor:
    pass  # Placeholder, ill add attributes and methods later

class Sensor:
    def __init__(self, id, is_active=False, car_park=None):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor {self.id}: {'Active' if self.is_active else 'Inactive'}"

class EntrySensor(Sensor):
    pass

class ExitSensor(Sensor):
    pass
