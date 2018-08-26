'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string_):
    """tokenize"""
    adictionary_ = {}
    for i in string_:
        count_ = string_.count(i)
        if i not in adictionary_:
            adictionary_[i] = count_
    return adictionary_
def main():
    """tokenize"""

    number_ = int(input())
    for _ in range(number_):
        str_ = input()
        str_1 = re.split(', | "|",|\n| |";|', str_)

    print(tokenize(str_1))
if __name__ == '__main__':
    main()
