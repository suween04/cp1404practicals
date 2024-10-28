class ProgrammingLanguage:
    """Represents information about a programming language."""

    def __init__(self, name, typing, reflection, pointer_arithmetic, year):
        """Construct a ProgrammingLanguage from the given values.

        Args:
            name (str): The name of the language.
            typing (str): The typing discipline (e.g., static, dynamic, strong, weak).
            reflection (bool): Whether the language supports reflection.
            pointer_arithmetic (bool): Whether the language supports pointer arithmetic.
            year (int): The year the language first appeared.
        """

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.pointer_arithmetic = pointer_arithmetic
        self.year = year

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return (
            f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
            f"Pointer Arithmetic={self.pointer_arithmetic}, First appeared in {self.year}"
        )

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"