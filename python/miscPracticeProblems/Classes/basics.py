# -*- coding: utf-8 - *-

# Declare a Zombie class that accepts health and brains_eaten parameters.

# In the initialization process for a Zombie object, assign the
# two parameters to two attributes with the same name.
#
# If the instantiation does not pass a health parameter,
# it should be assigned a default value of 100.
#
# If the instantiation does not pass a brains_eaten parameter,
# it should be assigned a default value of 5.

# Instantiate a Zombie object with 80 health and 5 brains eaten.
# Assign it to a “bob” variable.
#
# Instantiate a Zombie object with 120 health and 3 brains eaten.
# Assign it to a “sally” variable.
#
# Instantiate a Zombie object with no custom parameters.
# Assign it to a “benjamin” variable.
#
# Practice instantiating the objects with both positional and keyword arguments.

class Zombie():
    def __init__(self, health=100, brains_eaten=5):
        self.health = health
        self.brains_eaten = brains_eaten


bob = Zombie(80)
sally = Zombie(health=120, brains_eaten=3)
benjamin = Zombie()


class Person():
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age

    def talk(self):
        print(
            f"Hi! My name is {self.first_name} and I'm {self.age} years old.")


saul = Person("Saul", 40)

saul.talk()
