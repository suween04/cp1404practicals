# Example 1: Format and print product details with price
guitar_name = "Gibson L-5 CES"
year = 1922
cost = 16036.0

# Using f-string formatting
print(f"{year} {guitar_name} for about ${cost:,.2f}!")

# Example 2: Using a for loop with f-string formatting to print powers of 2
for i in range(11):
    print(f"2 ^ {i:2} is {2 ** i:4}")
