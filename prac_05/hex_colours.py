HEX_COLOURS = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

def get_hex_code(colour_name):
    return HEX_COLOURS.get(colour_name.capitalize(), "Unknown colour")

def main():
    while True:
        colour_name = input("Enter a colour name (or blank to quit): ")
        if not colour_name:
            break
        print(f"The code for '{colour_name}' is {get_hex_code(colour_name)}")

if __name__ == "__main__":
    main()
