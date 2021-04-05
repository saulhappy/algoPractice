"""
A named vehicle with a sequence of pings.
"""


class Vehicle(object):

    def __init__(self, name):
        self.name = name
        self.pings = []

    def get_name(self):
        """
        The name of the vehicle.
        """
        return self.name

    def get_pings(self):
        """
        The pings for the vehicle, in chronological order (earliest first).
        """
        return self.pings

    def get_total_distance(self):
        """
        Determines the total distance traveled by the vehicle.
        """
        return get_total_distance(self.pings)

    def get_average_speed(self):
        """
        Determines the average speed of the vehicle.
        """
        # TODO: implement
        return 0.0

    def __str__(self):
        return str(self.name) + ": " + str(self.pings)

def get_total_distance(pings):
    """
    Determines the total distance covered by the pings.
    """
    # TODO: implement
    prev = None
    for ping in pings:
        # write a function that takes in a ping, 
        if prev is not None:
            if ping.position != prev.position:
                print(prev, ping)
        prev = ping 
    return 0.0
