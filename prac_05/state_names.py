STATE_NAMES = {
    "NSW": "New South Wales",
    "QLD": "Queensland",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

def get_state_name(state_code):
    try:
        return STATE_NAMES[state_code.upper()]
    except KeyError:
        return "Invalid state code"

def main():
    state_code = input("Enter short state: ").upper()
    print(f"{state_code} is {get_state_name(state_code)}")

    for code, name in STATE_NAMES.items():
        print(f"{code:<3} is {name}")

if __name__ == "__main__":
    main()
