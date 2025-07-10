def total_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    character_counts = {}

    for char in text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    return character_counts

def sorted_counts(character_counts):
    char = character_counts
    char.sort(key=character_counts, reverse=True)
    return char


def sorted_counts(character_counts):
    dictionary = []
    for char in character_counts:
        dictionary.append({"char": char, "num": character_counts[char]})
    dictionary.sort(key=lambda x: x["num"], reverse=True)
    return dictionary