# exceptions_demo.py

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # Check if the denominator is zero to prevent ZeroDivisionError
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:  # This will not trigger anymore with the check above
    print("Cannot divide by zero!")  # Kept for safety
print("Finished.")

"""
Questions:

1. When will a ValueError occur?
- A ValueError occurs when the input cannot be converted to an integer. This happens if the user enters something 
that isn't a valid integer, such as a string (e.g., "abc") or a floating-point number (e.g., "3.14").

2. When will a ZeroDivisionError occur?
- A ZeroDivisionError occurs when the user inputs `0` as the denominator and the program tries to divide by zero. 
 This causes the division operation to fail since dividing by zero is undefined.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
- Yes, you can check if the denominator is zero before attempting the division. If the denominator is zero, 
the program should print a message and avoid performing the division. In the updated code above, this is done 
using an `if denominator == 0:` check before performing the division.
"""
