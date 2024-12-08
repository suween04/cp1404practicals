# list_comprehensions.py

# Starting list
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# List comprehensions based on TODO instructions
squared_numbers = [x**2 for x in numbers]
print("Squared numbers:", squared_numbers)

even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# Example of more list comprehensions if needed
unique_numbers = [x for x in set(numbers)]
print("Unique numbers:", unique_numbers)
