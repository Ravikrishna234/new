"""GCD iteration python"""
def gcdIter(a, b):
    """gcd"""
    if a > b:
        num = a
        den = b
    else:
        num = b
        den = a
    rem = num % den
    while rem != 0:
        num = den
        den = rem
        rem = num % den
    return den
def main():
    """gcd"""
    data = input()
    data = data.split()
    print(gcdIter(int(data[0]),int(data[1]))) 

if __name__ == "__main__":
    main()
