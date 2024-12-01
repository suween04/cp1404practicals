from car import Car
import random

class UnreliableCar(Car):
    """Specialised version of a Car that has reliability."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
