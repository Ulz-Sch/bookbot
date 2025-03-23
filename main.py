from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def main():
    try:
        if len(sys.argv) == 2 :
            print(sys.argv[1])
            path = sys.argv[1]
            book = get_book_text(path)
            num_of_words = get_number_words(book)
            count_words = get_count_words(book)
            sorted_letter_count = get_sorted_dict(count_words)

            print_stats(path,num_of_words,sorted_letter_count)
        else:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

    except IsADirectoryError:
        print("Invalid Path.")

main()