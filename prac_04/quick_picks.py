# quick_picks.py
import random

NUMBERS_IN_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def generate_quick_picks(number_of_picks):
    """Generate specified number of quick picks."""
    for _ in range(number_of_picks):
        quick_pick = []
        while len(quick_pick) < NUMBERS_IN_PICK:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in quick_pick:
                quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{num:2}" for num in quick_pick))

def main():
    number_of_picks = int(input("How many quick picks? "))
    generate_quick_picks(number_of_picks)

if __name__ == "__main__":
    main()
