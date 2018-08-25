'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import string
SMALL_ = string.ascii_lowercase
Capital_ = string.ascii_uppercase
NUMBER_ = '0123456789'
def clean_string(string_):
    """clean"""
    string1_ = ''
    for i in string_:
    	if i in SMALL_ or i in NUMBER_:
    		string1_ = string1_ + i
    return string1_


def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
