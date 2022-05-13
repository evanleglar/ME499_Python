#!/usr/bin/env python3
import sys
import string


def txt_clean(txt_file):
    """
    function to change all characters in string to lower-case, then use translate table to remove all punctuation,
    and then split the string by the delimiter spaces. The output is an iterable, clean list
    """
    with open(txt_file, 'r') as f_1:
        txt_file = f_1.read()

    txt_file = txt_file.lower()  # converts each string into lower case letters
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^’&*_~'''  # list of punctuation to clean from txt (includes extra ’ )
    txt_file = txt_file.translate(str.maketrans('', '', string.punctuation + punctuations))  # removes the punctuation
    clean_list = txt_file.split()  # splits each text file based on spaces found
    return clean_list


def word_count(txt_file):
    """
    function to return the cleaned list as a list named num_words
    """
    num_words = txt_clean(txt_file)
    return num_words


def unique_count(txt_file):
    """
    function to return an iterable list after duplicates have been removed by the set function
    """
    unique_words = list(set(txt_clean(txt_file)))
    return unique_words


def unique_compare(x, y):
    """
    takes in 2, cleaned lists from the original txt files and then uses the python set operations to determine what
    words are unique to each file and the intersection between the two
    """
    txt1 = set(txt_clean(x))
    txt2 = set(txt_clean(y))
    only_txt1 = list(txt1 - txt2)
    only_txt2 = list(txt2 - txt1)
    both_txt = txt1.intersection(txt2)
    return only_txt1, only_txt2, both_txt


if __name__ == '__main__':

    if len(sys.argv) == 3:
        x = sys.argv[1]
        y = sys.argv[2]
    elif len(sys.argv) == 1:
        x = "war_and_peace.txt"
        y = "words.txt"
    else:
        raise ValueError

    print(str(x) + ":")
    print("  " + str(len(word_count(x))) + " words")
    print("  unique: " + str(len(unique_count(x))))
    print(str(y) + ":")
    print("  " + str(len(word_count(y))) + " words")
    print("  unique: " + str(len(unique_count(y))))

    j, k, m = unique_compare(x, y)
    print("Only war_and_peace.txt: " + str(len(j)))
    print("Only words.txt: " + str(len(k)))
    print("Both files: " + str(len(m)))
