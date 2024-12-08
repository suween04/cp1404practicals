import random

def main():
    """Main function to display menu and handle user choices."""
    score = get_valid_score()
    choice = ""

    while choice != "Q":
        print("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Score: {score} is {determine_result(score)}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Goodbye!")
        else:
            print("Invalid choice.")


def get_valid_score():
    """Get a valid score between 0 and 100."""
    score = int(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Try again.")
        score = int(input("Enter a valid score (0-100): "))
    return score


def determine_result(score):
    """Determine the result based on the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Display stars equivalent to the score."""
    print('*' * score)


main()
