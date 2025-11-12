class CarPark():
    def __init__(self, location, capacity, plates=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates
        self.displays = displays or []

    def __str__(self):
        return f"Car is parked at {self.location}, with {self.capacity} bays available."