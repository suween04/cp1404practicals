def main():
    choice = ""

    while choice != "Q":
        print("C - Convert Celsius to Fahrenheit")
        print("F - Convert Fahrenheit to Celsius")
        print("Q - Quit")

        choice = input(">>> ").upper()

        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print(f"Result: {celsius:.2f} C")
        elif choice != "Q":
            print("Invalid option")

    print("Thank you.")


if __name__ == "__main__":
    main()
