"""special characters"""
def main():
    """special"""
    st_in = input()
    s_st = ''
    for i in st_in:
        if i in '!@#$%^&*':
            s_st = s_st + " "
        else:
            s_st = s_st + i
    print(s_st)
if __name__ == "__main__":
    main()
