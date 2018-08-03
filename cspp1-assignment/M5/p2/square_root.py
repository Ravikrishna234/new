"""squareroot"""
def main():
    """square"""
    sq_in = int(input())
    cons_tant = 0.01
    st_art = 0.0
    in_cr = 0.1
    while abs(st_art**2 - sq_in) >= cons_tant and st_art <= sq_in:
        st_art += in_cr
    if abs(st_art**2 - sq_in) >= cons_tant:
        print('Failed on cube root of', sq_in)
    else:
        print(st_art, 'is close to the square root of', sq_in)

if __name__ == "__main__":
    main()
    