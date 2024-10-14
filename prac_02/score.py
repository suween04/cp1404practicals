import random

def main():
    """Main function to get score and print result."""
    score = float(input("Enter your score: "))
    result = determine_result(score)
    print(f"Your result is: {result}")

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score} is {determine_result(random_score)}")


def determine_result(score):
    """Determine the result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
