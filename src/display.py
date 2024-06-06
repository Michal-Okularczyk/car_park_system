class Display:
    def __init__(self, display_id, message="", is_on=False, car_park=None):
        self.display_id = display_id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"Display {self.display_id}: {self.message}"

    def update(self, data):
        if "message" in data:
            self.message = data["message"]
        if "is_on" in data:
            self.is_on = data["is_on"]

