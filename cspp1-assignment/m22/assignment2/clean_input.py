"""Write a function to clean up a given string by removing the special characters and retain"""
import string
SMALL_ = string.ascii_lowercase
NUMBER_ = '0123456789'
def clean_string(string_):
    """clean"""
    string1_ = ''
    for i in string_:
        if i in SMALL_ or i in NUMBER_:
            string1_ = string1_ + i
    return string1_


def main():
    """clean"""
    string_ = input()
    print(clean_string(string_))

if __name__ == '__main__':
    main()
