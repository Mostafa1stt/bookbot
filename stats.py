def get_num_words(contents):
    list_of_words = contents.split()

    return len(list_of_words)


def get_num_letter(contents):
    letter_dic = {}

    for letter in contents.lower():
        if letter in letter_dic:
            letter_dic[letter] += 1
        else:
            letter_dic[letter] = 1

    return letter_dic


def sort_on(item):
    return item["num"]


def list_of_dic(contents):
    list_of_dictionary = []
    dic = get_num_letter(contents)

    for key in dic:
        if key.isalpha():
            list_of_dictionary.append({"char": key, "num": dic[key]})

    list_of_dictionary.sort(reverse=True, key=sort_on)

    return list_of_dictionary
