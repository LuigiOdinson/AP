"""A set of classes that can be used to represent electric cars"""
from car import Car
# we import the Car class because it's the parent of the ElectricCar class


# Battery Class
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWH battery")

    def get_range(self):
        if self.battery_size == 75:
            car_range = 260
        elif self.battery_size == 100:
            car_range = 315
        print(f"This can go about {car_range} miles in a full charge")


# Electric Car Class
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
