def extract_name(email):
    parts = email.split("@")[0].split(".")
    name = " ".join(parts).title()
    return name

def main():
    emails = {}
    email = input("Email: ")
    while email:
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation != "y" and confirmation != "":
            name = input("Name: ")
        emails[email] = name
        email = input("Email: ")

    for email, name in emails.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
