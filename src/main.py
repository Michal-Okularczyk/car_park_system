from pathlib import Path
from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

def main():
    # Create a car park object with location "moondalup", capacity 100, and log_file "moondalup.txt"
    car_park = CarPark(location="moondalup", capacity=100, log_file=Path("moondalup.txt"))

    # Create an entry sensor object with id 1, is_active True, and car_park car_park
    entry_sensor = EntrySensor(sensor_id=1, is_active=True, car_park=car_park)

    # Create an exit sensor object with id 2, is_active True, and car_park car_park
    exit_sensor = ExitSensor(sensor_id=2, is_active=True, car_park=car_park)

    # Create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
    display = Display(display_id=1, message="Welcome to Moondalup", is_on=True, car_park=car_park)

    # Register sensors and display with the car park
    try:
        car_park.register(entry_sensor)
        car_park.register(exit_sensor)
        car_park.register(display)
    except TypeError as e:
        print(e)

    # Simulate cars entering the car park
    for _ in range(10):
        entry_sensor.detect_vehicle()

    # Simulate cars exiting the car park
    for _ in range(2):
        exit_sensor.detect_vehicle()

if __name__ == "__main__":
    main()
