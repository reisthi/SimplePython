"""Namedtuples allow you to define reusable blueprints"""

from collections import namedtuple

Car = namedtuple('Car', 'color mileage automatic')
car_one = Car('red', 444.90, True)
print(car_one)  # Car(color='red', mileage=444.9, automatic=True)

# accessing fields
print(car_one.color)  # 'red'

# named tuples are immutable
car_one.automatic = False
# AttributeError: can't set attribute
