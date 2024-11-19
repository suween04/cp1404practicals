from guitar import Guitar

def main():
    """Read guitars from a file, display them, sort them, and display them again."""
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        name, year, cost = line.strip().split(",")
        try:
            # Handle potential conversion errors (e.g., invalid year or cost)
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
        except ValueError:
            print(f"Error: Invalid data in line: {line}")
    in_file.close()

    # Display guitars
    print("Guitars:")
    for guitar in guitars:
        print(guitar)

    # Sort guitars by year
    guitars.sort()

    # Display sorted guitars
    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)

if __name__ == "__main__":
    main()