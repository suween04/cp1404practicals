# total_income.py

def get_monthly_incomes():
    """Collect monthly incomes from the user."""
    months_count = int(input("How many months? "))
    incomes = []
    for month in range(1, months_count + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes

def print_income_report(incomes):
    """Print a report of incomes with cumulative totals."""
    print("Income Report\n-------------")
    cumulative_total = 0
    for month, income in enumerate(incomes, start=1):
        cumulative_total += income
        print(f"Month {month:2} - Income: ${income:10.2f}  Total: ${cumulative_total:10.2f}")

def main():
    incomes = get_monthly_incomes()
    print_income_report(incomes)

if __name__ == "__main__":
    main()
