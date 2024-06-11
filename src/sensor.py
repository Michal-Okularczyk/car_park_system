class Sensor:
    def __init__(self, sensor_id, is_active=False, car_park=None):
        self.sensor_id = sensor_id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor {self.sensor_id}: {'Active' if self.is_active else 'Inactive'}"

    def update(self, data):
        if "is_active" in data:
            self.is_active = data["is_active"]



