"""digit product"""
def main():
    """digit"""
    num_in = int(input())
    product_st = 1
    while num_in > 0:
        di_git = num_in % 10
        product_st = product_st * di_git
        num_in = num_in // 10
    print(product_st)
if __name__ == "__main__":
    main()
