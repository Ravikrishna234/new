"""SUM OF DIGITS"""
def sumofdigits(n_input):
    """digits"""
    if n_input == 0:
        return 0
    return n_input % 10 + sumofdigits(n_input // 10)
def main():
    """digits"""
    a_in = input()
    print(sumofdigits(int(a_in)))
if __name__ == "__main__":
    main()
