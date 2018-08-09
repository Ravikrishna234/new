"""SORTED"""
def get_available_letters(letters_guessed):
    """sort"""
    import string
    st_r = ''
    co_unt = dict((key, 0) for key in string.ascii_lowercase)
    for char in co_unt.keys():
        if char not in letters_guessed:
            st_r = st_r + char
    return st_r
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
