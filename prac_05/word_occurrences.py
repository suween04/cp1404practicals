def count_word_occurrences(text):
    word_counts = {}
    words = text.split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def main():
    text = input("Text: ")
    word_counts = count_word_occurrences(text)
    longest_word_length = max(len(word) for word in word_counts)
    for word in sorted(word_counts):
        print(f"{word:{longest_word_length}} : {word_counts[word]}")

if __name__ == "__main__":
    main()
