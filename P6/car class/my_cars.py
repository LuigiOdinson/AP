from car import Car
from electric_car import ElectricCar as EC

my_audi = Car('audi', 'a4', 2019)
my_tesla = EC('tesla', 'model s', 2020)

print(my_audi.get_descriptive_name())
print(my_tesla.get_descriptive_name())
