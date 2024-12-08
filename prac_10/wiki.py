"""
wiki.py
"""
import wikipedia


def fetch_wikipedia_page():
    """Prompt the user for a Wikipedia page title or search phrase."""
    while True:
        query = input("Enter page title (or blank to quit): ")
        if not query.strip():
            print("Thank you.")
            break
        try:
            page = wikipedia.page(query, autosuggest=True)
            print(f"\n{page.title}\n{page.summary[:500]}...\n{page.url}\n")
        except wikipedia.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.PageError:
            print(f"Page id \"{query}\" does not match any pages. Try another id!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    fetch_wikipedia_page()
