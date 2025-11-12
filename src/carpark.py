from sensor import Sensor
from display import Display

class CarPark():
    def __init__(self, location, capacity, plates=None, displays=None, sensors=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates
        self.displays = displays or []
        self.sensors = sensors or []

    def __str__(self):
        return f"Car is parked at {self.location}, with {self.capacity} bays available."

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)
