from warehouse_server import WarehouseServer


def main():
    # Initialize WarehouseServer instance.
    warehouse_server = WarehouseServer()
    warehouse_server.initialize_server("warehouse_pings.csv")
    print("~~~WarehouseServer is initialized.")
    print(f"Total distance: {warehouse_server.vehicles[0].get_total_distance()}")
    print("")

    print("Average Speeds: " + str(warehouse_server.get_average_speeds()))
    print("")

    print("The 3 most traveled vehicles since 1553273158 are: ")
    print(warehouse_server.get_most_traveled_since(3, 1553273158))

    print("Vehicles possibly damaged: ")
    print(warehouse_server.check_for_damage())

    # Feel free to put any print statements below for testing and debugging


if __name__ == "__main__":
    main()
