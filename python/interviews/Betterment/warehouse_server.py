import csv
from ping import Ping
from vehicle import Vehicle


class WarehouseServer(object):

    def __init__(self):
        # vehicles is a list of vehicle instances
        self.vehicles = []

    def get_average_speeds(self):
        """
        Returns a dictionary from vehicle name to that vehicle's average speed
        for all vehicles.
        """
        avg_speeds = {}
        for vehicle in self.vehicles:
            avg_speeds[vehicle.get_name()] = vehicle.get_average_speed()
        return avg_speeds

    def get_most_traveled_since(self, max_results, timestamp):
        """
        Returns a sorted list of size max_results of vehicle names
        corresponding to the vehicles that have traveled the most distance since
        the given timestamp.
        """
        # TODO: Implement
        return []

    def check_for_damage(self):
        """
        Returns a list of names identifying vehicles that might have been damaged
        through any number of risky behaviors, including collision with another
        vehicle and excessive acceleration.
        """
        # TODO: implement
        return []

    def initialize_server(self, file_name):
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for parsed_line in reader:
                self.process_ping(
                            parsed_line[0],
                            float(parsed_line[1]),
                            float(parsed_line[2]),
                            int(parsed_line[3]))

    def process_ping(self, vehicle_name, x, y, timestamp):
        ping = Ping(x, y, timestamp)
        if len(self.vehicles) == 0 or vehicle_name != self.vehicles[-1].get_name():
            self.vehicles.append(Vehicle(vehicle_name))
        self.vehicles[-1].get_pings().append(ping)
