def main():
    """Main function to get password and print stars."""
    password = get_password()
    print_stars(password)


def get_password():
    """Get and validate password from the user."""
    password = input("Enter your password: ")
    while len(password) < 5:  # You can set your own validation rule here
        print("Password too short!")
        password = input("Enter a valid password: ")
    return password


def print_stars(password):
    """Print stars equal to the length of the password."""
    print('*' * len(password))


main()
