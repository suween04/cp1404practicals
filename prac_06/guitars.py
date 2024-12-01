from prac_06.guitar import Guitar

# List to store Guitar instances
guitars = []

# Adding guitars to the list (you can uncomment the input section for interactive input)
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))
guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

# Printing the details of the guitars
print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
