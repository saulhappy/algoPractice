# -*- coding: utf-8 - *-

# Define a Car class that accepts a maker (string), model (string),
# and year (number) parameters and assigns them to respective
# attributes

# Define a Dealership class. Each Dealership object should instantiate
# with a "cars" attribute set to an empty list.

# A Dealership object should have a accept_delivery instance method
# that accepts a Car object and adds it to the Dealership's internal
# "cars" list

# Indexing into a Dealership with a number should access a specific
# Car object in the Dealership.

# An index position in a Dealership should also be overwriteable
# with a new Car object (see examples below)

# f150 = Car(maker = "Ford", model = "F-150", year = 2019)
# camry = Car(maker = "Toyota", model = "Camry", year = 2020)
# porsche = Car (maker = "Porsche", model = "911 Carrera", year = 2021)

# dealership = Dealership()

# dealership.accept_delivery(f150)
# dealership.accept_delivery(camry)

# print(dealership[0].year) # 2019 -- the F150's year

# dealership[0] = porsche

# for car in dealership:
#   print(car.maker) # Porsche, Toyota
