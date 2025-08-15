from stats import get_num_words, list_of_dic
import sys


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    contents = get_book_text(path)
    num_words = get_num_words(contents)
    print(f"Found {num_words} total words")
    for i in list_of_dic(contents):
        print(f"{i["char"]}: {i["num"]}")


main()
