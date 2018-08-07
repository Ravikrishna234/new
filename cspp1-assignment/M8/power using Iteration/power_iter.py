"""iteration"""
def iterPower(base, exp):
    """iter"""
    result = 1
    while exp > 0:
        result = result * base
        exp = exp - 1
    return result


def main():
    """iteration"""
    data = input()
    data = data.split()
    print(iterPower(float(data[0]),int(data[1]))) 

if __name__ == "__main__":
    main()