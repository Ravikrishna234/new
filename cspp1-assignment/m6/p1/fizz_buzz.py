"""Fizz Buzz"""
def main():
    """Fizz"""
    n_in = int(input())
    for i in range(1, n_in+1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 or i % 5 == 0:
            print("Fizz")
            print("Buzz")
        else:
            print(i)
if __name__ == "__main__":
    main()
