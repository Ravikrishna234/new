"""factorial of number"""
def factorial(n_input):
    """fact"""
    if n_input == 0:
        return 1
    return n_input * factorial(n_input - 1)
def main():
    """fact"""
    a_input = input()
    print(factorial(int(a_input)))
if __name__ == "__main__":
    main()
