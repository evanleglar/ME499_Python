#!/usr/bin/env python


def letter_count(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    return str1.count(str2)


if __name__ == '__main__':
    str1 = 'helLoworLd'
    str2 = 'L'
    print("Total number of letter " + str2 + " is " + str(letter_count(str1, str2)))


