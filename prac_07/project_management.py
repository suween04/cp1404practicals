from project import Project

def main():
  """Manage projects: Add, display, search."""
  projects = []

  # Interactive menu loop
  while True:
    print("\nProject Management System")
    print("1. Add Project")
    print("2. Display All Projects")
    print("3. Search Project by Name")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
      name = input("Enter project name: ")
      start_date = input("Enter start date (DD/MM/YYYY): ")
      while True:
        try:
          priority = int(input("Enter project priority (integer): "))
          break
        except ValueError:
          print("Invalid priority. Please enter an integer.")
      while True:
        try:
          cost_estimate = float(input("Enter cost estimate (float): "))
          break
        except ValueError:
          print("Invalid cost estimate. Please enter a number.")
      while True:
        try:
          completion_percentage = int(input("Enter completion percentage (integer): "))
          if 0 <= completion_percentage <= 100:
            break
          else:
            print("Invalid completion percentage. Enter a value between 0 and 100.")
        except ValueError:
          print("Invalid completion percentage. Please enter an integer.")
      project = Project(name, start_date, priority, cost_estimate, completion_percentage)
      projects.append(project)
      print(f"Project '{name}' added successfully!")

    elif choice == '2':
      if not projects:
        print("No projects found.")
      else:
        print("\nAll Projects:")
        for project in projects:
          print(project)

    elif choice == '3':
      search_name = input("Enter project name to search: ")
      found_projects = []
      for project in projects:
        if search_name.lower() in project.name.lower():
          found_projects.append(project)
      if found_projects:
        print("\nMatching Projects:")
        for project in found_projects:
          print(project)
      else:
        print(f"No project found with the name '{search_name}'.")

    elif choice == '4':
      print("Exiting Project Management System.")
      break

    else:
      print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
  main()