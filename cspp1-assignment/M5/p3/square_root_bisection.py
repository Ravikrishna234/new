"""square_root_bisection"""
def main():
    """square"""
    sq_in = int(input())
    cons_tant = 0.01
    a_in = 0.0
    b_in = sq_in
    c_out = (b_in + a_in)/2.0
    while abs(c_out**2 - sq_in) >= cons_tant:
        if c_out**2 < sq_in:
            a_in = c_out
        else:
            b_in = c_out
        c_out = (b_in + a_in)/2.0
    print(str(c_out))

if __name__ == "__main__":
    main()
