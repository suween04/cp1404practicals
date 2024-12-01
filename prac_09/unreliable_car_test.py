from unreliable_car import UnreliableCar

def main():
    unreliable_car = UnreliableCar("Dodgy", 100, 50)
    for i in range(10):
        print(f"Attempt to drive 10km: Drove {unreliable_car.drive(10)}km")
    print(unreliable_car)

if __name__ == "__main__":
    main()
