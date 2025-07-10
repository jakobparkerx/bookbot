from stats import total_words
from stats import count_characters
from stats import sorted_counts
import sys

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)




def get_book_text(file_path):
    file_path = sys.argv[1]
    with open(file_path) as file:
        return file.read()
    
    
def main():
    text = get_book_text("books/frankenstein.txt")
    length = total_words(text)
    characters = count_characters(text)
    sorted_characters = sorted_counts(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {length} total words")
    print("--------- Character Count -------")
    for characters in sorted_characters:
        character = characters["char"]
        number = characters["num"]
        if character.isalpha():
            print(f"{character}: {number}")
    print("============= END ===============")



main()
 

