from stats import get_num_words, list_of_dic


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    contents = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(contents)
    print(f"Found {num_words} total words")
    for i in list_of_dic(contents):


main()
