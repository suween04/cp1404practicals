import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.00      # The minimum stock price
MAX_PRICE = 100.00    # The maximum stock price
INITIAL_PRICE = 10.00  # The starting price
FILENAME = "capitalist_conrad_output.txt"  # Output file name

# Open file for writing
out_file = open(FILENAME, 'w')

# Start with the initial price
price = INITIAL_PRICE
number_of_days = 0

# Print starting price to the file
print(f"Starting price: ${price:,.2f}", file=out_file)

# Simulate the stock price changes
while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1  # Increment the day count

    # Determine if the price increases or decreases
    if random.randint(1, 2) == 1:  # 50% chance
        # Increase the price by a random percentage between 0 and MAX_INCREASE
        price_increase = random.uniform(0, MAX_INCREASE)
        price *= (1 + price_increase)
    else:
        # Decrease the price by a random percentage between 0 and MAX_DECREASE
        price_decrease = random.uniform(0, MAX_DECREASE)
        price *= (1 - price_decrease)

    # Print the price for the day to the file
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Close the file at the end
out_file.close()
