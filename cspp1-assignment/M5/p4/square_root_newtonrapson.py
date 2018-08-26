"""Square root newton rapson"""
def main():
    """newton"""
    constant_ = 0.01
    square_input = int(input())
    startvalue_ = square_input/2.0
    while abs(startvalue_*startvalue_ - square_input) >= constant_:
        startvalue_ = startvalue_ - (((startvalue_**2) - square_input)/(2*startvalue_))
    print(str(startvalue_))

if __name__ == "__main__":
    main()
