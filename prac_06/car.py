class Car:
    def __init__(self, name, fuel=100, odo=0):
        self.name = name
        self.fuel = fuel
        self.odo = odo

    def drive(self, distance):
        if distance < 0:
            print("Distance must be >= 0")
            return
        if distance > self.fuel:
            distance = self.fuel  # Drive as far as possible
        self.odo += distance
        self.fuel -= distance
        print(f"The car drove {distance}km.")
        if self.fuel == 0:
            print("The car ran out of fuel.")

    def refuel(self, amount):
        if amount < 0:
            print("Fuel amount must be >= 0")
            return
        self.fuel += amount
        print(f"Added {amount} units of fuel.")

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odo={self.odo}"
