from programming_language import ProgrammingLanguage

# Creating ProgrammingLanguage instances
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Printing the string representation of the Python instance
print(python)

# List of ProgrammingLanguage objects
languages = [python, ruby, visual_basic]

# Printing dynamically typed languages
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
