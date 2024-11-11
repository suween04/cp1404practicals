class ProgrammingLanguage:
    """Represents a programming language with its core features."""

    def __init__(self, name, typing, reflection, paradigm):
        """
        Initializes a ProgrammingLanguage object.

        Args:
            name (str): The name of the language.
            typing (str): The typing discipline (e.g., static, dynamic, strong, weak).
            reflection (bool): Whether the language supports reflection.
            paradigm (str): The primary programming paradigm (e.g., imperative, object-oriented, functional).
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.paradigm = paradigm

    def __str__(self):
        """Returns a string representation of the language."""
        return f"{self.name} ({self.typing}, Reflection={self.reflection}, Paradigm={self.paradigm})"