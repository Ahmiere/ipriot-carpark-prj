import carpark
from carpark import CarPark

class Display:
    def __init__(self, id, message="", is_on=False, car_park=None):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = carpark.CarPark


    def __str__(self):
        return f"Display {self. id}: {self.message}"

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")
