
"""vowels counter"""
def main():

    """vowels"""
    v_input = input()
    vowel_c = 0
    cons_c = 0
    for i in v_input:
        if i in 'aeiou':
            vowel_c = vowel_c + 1
        else:
            cons_c = cons_c + 1

    # print("Number of vowels:")
    print(vowel_c)


if __name__ == "__main__":
    main()
