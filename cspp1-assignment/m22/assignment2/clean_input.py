'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import string
small_ = string.ascii_lowercase
cap_ = string.ascii_uppercase
def clean_string(string_):
    """clean"""
    string1_ = ''
    for i in string_:
    	if i in small_:
    		string1_ = string1_ + i
    return string1_


def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
