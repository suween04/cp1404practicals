import csv
from collections import namedtuple

from prac_07.programming_language import ProgrammingLanguage


class ProgrammingLanguage:
    """Represents a programming language."""

    def __init__(self, name, typing, reflection):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage instance."""
        return f"{self.name}, {self.typing}, Reflection={self.reflection}"


def main():
    """Read language data from a file and create ProgrammingLanguage objects."""
    languages = []
    in_file = open("languages.csv", "r")
    in_file.readline()  # Skip the header line
    for line in in_file:
        parts = line.strip().split(",")
        language = ProgrammingLanguage(parts[0], parts[1], parts[2] == "True")
        languages.append(language)
    in_file.close()

    for language in languages:
        print(language)


if __name__ == "__main__":
    main()