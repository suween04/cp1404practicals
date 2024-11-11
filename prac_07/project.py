class Project:
    """Represents a project with its details."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project object.

        Args:
            name (str): The name of the project.
            start_date (str): The start date of the project in DD/MM/YYYY format.
            priority (int): The priority level of the project.
            cost_estimate (float): The estimated cost of the project.
            completion_percentage (int): The percentage completion of the project.
        """

        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Returns a string representation of the project."""
        return f"{self.name}, Start: {self.start_date}, Priority: {self.priority}, " \
               f"Cost: ${self.cost_estimate:.2f}, Completion: {self.completion_percentage}%"