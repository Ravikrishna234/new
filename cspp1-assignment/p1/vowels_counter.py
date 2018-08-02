"""vowels counter"""
def main():
    """vowels"""
    vol_inp = input("Enter a string")
    vol_c = 0
    cons_str = 0
    for i in vol_inp:
        if i in 'aeiou':
            vol_c = vol_c + 1
        else:
            cons_str = cons_str + 1
    print("Number of volwels:")
    print(str(vol_c))
if __name__ == "__main__":
    main()
