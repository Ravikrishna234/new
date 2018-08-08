"""WORDS"""
def get_guessed_word(secret_word, letters_guessed):
    """word"""
    st_r = ''
    for i in secret_word:
        if i not in letters_guessed:
            st_r = st_r + '_'
        else:
            st_r = st_r + i
    return st_r
def main():
    """word"""
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    print(get_guessed_word(secret_word, list1))

if __name__ == "__main__":
    main()
