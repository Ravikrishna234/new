'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    """sort"""
    list_ = sorted(dictionary.keys())
    j = 0
    for i in list_:
        value = dictionary[i]
        print(str(list_[j]+" - "+str(value)))
        j = j + 1


def main():
    """sort"""
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
