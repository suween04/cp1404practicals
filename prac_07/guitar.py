class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name, year, cost):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar instance."""
        return f"{self.name} ({self.year}), worth ${self.cost:.2f}"

    def __lt__(self, other):
        """Less than, used for sorting Guitars by year."""
        return self.year < other.year