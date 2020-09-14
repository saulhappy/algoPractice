# -*- coding: utf-8 - *-

# You are writing a Python program to model a remote control
# for a television set. Declare a stations_to_numbers
# function that accepts a dictionary. The keys will be
# channel numbers and the values will be the station names.
# For example...
channels = {
    2: "CBS",
    4: "NBC",
    5: "FOX",
    7: "ABC"
}
# The stations_to_numbers function should return an
# inverted dictionary where the keys are the station names
# and the values are the channel numbers
#
# stations_to_numbers(channels) => {'CBS': 2, 'NBC': 4, 'FOX': 5, 'ABC': 7}


def stations_to_numbers(channels):
    return {num: channel for channel, num in channels.items()}


print(stations_to_numbers(channels))
