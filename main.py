import sys
from stats import get_num_words
from stats import count_characters


def get_book_text(filepath):
    print("Analyzing book found at", filepath, "\n")
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main(filepath):
    print(get_book_text(filepath))


def last_execution (filepath):
    print("============ BOOKBOT ============ \n")
    book_string = get_book_text(f'./{filepath}')
    print("----------- Word Count ----------\n")
    get_num_words(book_string)
    print("----------- Character Count ----------\n")
    count_characters(book_string)
    print("----------- End ----------")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
last_execution(sys.argv[1])
