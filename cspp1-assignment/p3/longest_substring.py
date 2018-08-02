"""largest subsequence"""
def main():
    """largest"""
    a_input = input()
    long_sub = 0
    ct_cr = 0
    maximum_c = 0
    for i in range(len(a_input)-1):
        if a_input[i] <= a_input[i+1]:
            ct_cr += 1
        else:
            ct_cr = 0
        if long_sub < ct_cr:
            long_sub = ct_cr
            maximum_c = i
    d_max = maximum_c - long_sub + 1
    print(a_input[d_max:d_max+long_sub+1])

if __name__ == "__main__":
    main()
