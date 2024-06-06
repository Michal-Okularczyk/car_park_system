# display.py

class Display:
    pass  # Placeholder, ill add attributes and methods later

class Display:
    def __init__(self, id, message="", is_on=False, car_park=None):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"Display {self.id}: {self.message}"

    def update(self, available_bays):
        self.message = f"{available_bays} bays available"
        if self.is_on:
            print(self)


