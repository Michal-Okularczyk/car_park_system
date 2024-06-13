class Display:
    def __init__(self, display_id, message, is_on, car_park):
        self.display_id = display_id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def update_message(self, message):
        self.message = message

    def toggle_display(self, status):
        self.is_on = status
