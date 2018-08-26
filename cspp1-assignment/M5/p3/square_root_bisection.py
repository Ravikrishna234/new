"""square_root_bisection"""
def main():
    """square"""
    square_input = int(input())
    constant_ = 0.01
    start_value = 0.0
    temp_ = square_input
    check_ = (temp_ + start_value)/2.0
    while abs(check_**2 - square_input) >= constant_:
        if check_**2 < square_input:
            start_value = check_
        else:
            temp_ = check_
        check_ = (temp_ + start_value)/2.0
    print(str(check_))

if __name__ == "__main__":
    main()
