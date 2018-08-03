# Write a python program to find the square root of the given number 
# using approximation method
"""squareroot"""
def main():
    """square"""
    sq_in=int(input())
    epsilon = 0.01
    guess = 0.0
    incr = 0.01
    num_guesses = 0
    while abs(guess**2 - sq) >= epsilon and guess <= sq:
        guess += incr
        num_guesses += 1
    if abs(guess**2 - sq) >= epsilon:
        print('Failed on cube root of', sq)
    else:
        print(guess, 'is close to the square root of', sq)

if __name__ == "__main__":
    main()