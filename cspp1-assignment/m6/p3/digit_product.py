"""digit product"""
def main():
    """digit"""
    num_in = int(input())
    temp_in = num_in
    if num_in < 0:
        num_in = -num_in
    product_st = 1
    while num_in > 0:
        di_git = num_in % 10
        product_st = product_st * di_git
        num_in = num_in // 10
        if temp_in < 0:
            product_st=-product_st
        elif temp_in == 0:
            print(temp_in)
        else:
            print(product_st)
if __name__ == "__main__":
    main()
