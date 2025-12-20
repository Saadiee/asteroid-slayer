import sys
from stats import get_word_count, get_letter_count, sorted_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_string = sys.argv[1]
    frankenstein_text = get_book_text(path_string)
    word_count = get_word_count(frankenstein_text)
    letter_count = get_letter_count(frankenstein_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_string}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_dict(letter_count)
    print("============= END ===============")
main()