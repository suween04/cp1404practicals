import csv

def load_wimbledon_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        return list(reader)

def process_champions(data):
    champions = {}
    for row in data:
        champion = row[2]
        champions[champion] = champions.get(champion, 0) + 1
    return champions

def get_countries(data):
    countries = {row[1] for row in data}
    return sorted(countries)

def main():
    data = load_wimbledon_data("wimbledon.csv")
    champions = process_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")

    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(countries))

if __name__ == "__main__":
    main()
