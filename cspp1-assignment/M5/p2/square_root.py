"""squareroot"""
def main():
    """square"""
    square_input = int(input())
    constant_ = 0.01
    startvalue_ = 0.0
    increment_ = 0.1
    while abs(startvalue_**2 - square_input) >= constant_ and startvalue_ <= square_input:
        startvalue_ += increment_
    if abs(startvalue_**2 - square_input) >= constant_:
        print('Failed on cube root of', square_input)
    else:
        print(startvalue_)

if __name__ == "__main__":
    main()
