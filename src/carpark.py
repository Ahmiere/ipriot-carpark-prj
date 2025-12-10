import json
from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime


class CarPark:
    def __init__(self, location, capacity, plates=None, displays=None, sensors=None, log_file=Path("log.txt"),
                 config_file="moondalup_config.json"):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)  # creates the file if it doesn't exist
        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        # create the configuration file if it doesn't exist:
        self.config_file.touch(exist_ok=True)

    def __str__(self):
        return f"Car is parked at {self.location}, with {self.capacity} bays available."

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()
            self._log_car_activity(plate, "exited")

        else:
            raise ValueError(f"Plate {plate} not found — cannot remove")

    def _log_car_activity(self, plate, action):
        """
            This function will open a file, and append the file to log details of the activity
            for each car

            parameters
            ----------
            self: An instance variable that allows this function to access other function
            within the CarPark class.
            plate: a 6 digit combination of letters and numbers that is unique for every car
            action: a string that explains whether the car is leaving or entering the car park

            Returns
            -------
            Nothing to the user interface, it only logs details regarding each car activities and
            leaves it in a log file for the car park.
            """
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def write_config(self):
        with self.config_file.open("w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    @classmethod
    def from_config(cls, config_file=Path("./moondalup_config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])

    @property
    def available_bays(self):
        result = self.capacity - len(self.plates)
        if result < 0:
            return 0
        else:
            return result
