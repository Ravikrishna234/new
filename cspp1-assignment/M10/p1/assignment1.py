"""SORTED"""
def get_available_letters(letters_guessed):
    """sort"""
    import string
    string_ = ''
    count_ = dict((key, 0)for key in string.ascii_lowercase)
    for char in count_.keys():
        if char not in letters_guessed:
            string_ = string_ + char
    return string_
def main():
    """sort"""
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))


if __name__ == "__main__":
    main()
