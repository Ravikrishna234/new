"""NUMBER"""
def main():

    """guess number"""

    print("Please think of a number between 0 and 100!")
    a_in = 0
    b_in = 100
    c_in = int((a_in + b_in) / 2)
    print("Is your secret number ", c_in)
    print("put h for high,put l for low,put c for correct")
    y_input = input()
    while y_input != 'c':
        if y_input == 'h':
            b_in = c_in
            c_in = int((a_in + b_in) / 2)
            print("Is your secret number", c_in)
            print("put h for high, put l for low, put c for correct")
            y_input = input()

        if y_input == 'l':
            a_in = c_in
            c_in = int((a_in + b_in) / 2)
            print("Is your secret number", c_in)
            print("put h for high,put l for low, put c for correct")
            y_input = input()

        if y_input != 'c':
            print("enter input correctly")
    if y_input == 'c':
        print("Game over. Your secret number", c_in)
if __name__ == "__main__":
    main()
