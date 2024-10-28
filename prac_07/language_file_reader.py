import csv
from collections import namedtuple

from prac_07.programming_language import ProgrammingLanguage

def main():
    """Read language data from a CSV file and create ProgrammingLanguage objects."""

    # Define a named tuple to represent language data
    LanguageTuple = namedtuple('LanguageTuple', 'name typing reflection pointer_arithmetic year')

    languages = []
    with open('languages.csv', 'r') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header row

        for row in reader:
            name, typing, reflection, pointer_arithmetic, year = row
            language = ProgrammingLanguage(name, typing, reflection == 'Yes', pointer_arithmetic == 'Yes', int(year))
            languages.append(language)

    for language in languages:
        print(language)

if __name__ == "__main__":
    main()