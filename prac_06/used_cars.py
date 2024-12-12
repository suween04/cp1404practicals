from prac_06.car import Car

def run_car_demo():
    """Sample code to demonstrate the functionality of the Car class."""
    my_vehicle = Car("My Vehicle", 180)  # Create an instance of Car
    my_vehicle.drive(30)  # Drive the vehicle for 30 km
    print(f"Remaining fuel: {my_vehicle.fuel}")  # Show remaining fuel
    print(my_vehicle)  # Print vehicle details

    limousine = Car("Limousine", 100)  # Create another Car instance
    limousine.refuel(20)  # Add 20 units of fuel to the limousine
    print(f"Fuel after refueling: {limousine.fuel}")  # Show fuel after refueling
    limousine.drive(115)  # Drive the limousine for 115 km
    print(limousine)  # Print limousine details

# Call the demo function
run_car_demo()
