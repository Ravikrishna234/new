"""GCD recursion python"""
def gcdRecur(a, b):
    """gcd"""
    if b != 0:
        return gcdRecur(b,a % b)
    else:
        return a
    


def main():
    """gcd"""
    data = input()
    data = data.split()
    print(gcdRecur(int(data[0]),int(data[1])))

if __name__ == "__main__":
    main()