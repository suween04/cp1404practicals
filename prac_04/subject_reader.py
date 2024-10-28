# subject_reader.py

def load_data(filename):
    """Load data from a file and return a list of lists."""
    data = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])  # Convert student numbers to integers
            data.append(parts)
    return data

def display_subject_details(data):
    """Display subject details in a readable format."""
    for subject_code, lecturer, student_count in data:
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")

def main():
    data = load_data('subject_data.txt')
    display_subject_details(data)

if __name__ == "__main__":
    main()
