from carpark import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


def main():

    car_park = CarPark("Moondalup", 100, log_file="moondalup.txt", config_file="moondalup_config.json")

    car_park = car_park.from_config()
# car_park is reinitialised using the moondalup_config.json file

    entry_sensor = EntrySensor(1, True, car_park)

    exit_sensor = ExitSensor(2, True, car_park)

    display_obj = Display(1, "Welcome to Moondalup", True, car_park)

    car_count = 0

    while car_count < 10:
        car_count = car_count + 1
        entry_sensor.detect_vehicle()

    while car_count > 8:
        car_count = car_count - 1
        exit_sensor.detect_vehicle()

if __name__ == '__main__':
    main()
