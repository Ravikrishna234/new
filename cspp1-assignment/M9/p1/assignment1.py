"""HANGMAN"""
def is_word_guessed(secret_word, letters_guessed):
    """man"""
    co_unt = 0
    len_gth = len(secret_word)
    for i in secret_word:
        if i in letters_guessed:
            co_unt += 1
    if co_unt == len_gth:
        return True
    return False
def main():
    """man"""
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
    print(is_word_guessed(secret_word, list1))

if __name__ == "__main__":
    main()
