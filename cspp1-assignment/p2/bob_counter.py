"""bob counter"""
def main():
    """bob"""
    a_input = input()
    co_tr = 0
    len_gth = len(a_input)
    sub_str = "bob"
    for i in range(len_gth):
        if sub_str == a_input[i:i+3]:
            co_tr = co_tr + 1
    print(co_tr)

if __name__ == "__main__":
    main()
