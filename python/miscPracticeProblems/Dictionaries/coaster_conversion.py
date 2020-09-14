# -*- coding: utf-8 - *-

# Declare a coaster_conversion function that accepts a dictionary
# The keys of the dictionary will be strings representing roller coasters
# The values will be the heights of each coaster in meters
#
# Return a new dictionary with the same keys.
# The values should be the heights converted from meters to feet,
# The final values (in feet) should also be rounded to the closest integer
# HINT: 1 meter is equal to 3.28084 feet
# HINT: The round function rounds a number to the nearest integer
#
coasters = {
    "Kingda Ka": 139,
    "Top Thrill Dragster": 130,
    "Superman: Escape From Krypton": 126
}
#
# coaster_conversion(coasters) => {'Kingda Ka': 456, 'Top Thrill Dragster': 426, 'Superman: Escape From Krypton': 413}


def coaster_conversion(coasters):
    return {coaster: int(round(meters * 3.28084)) for coaster, meters in coasters.items()}


print(coaster_conversion(coasters))
