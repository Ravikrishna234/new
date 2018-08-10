"""INTEGERDIVISION"""
def integer_division(x, a):
    """INT"""
    count = 0
    while x>=a:
        count += 1
        x = x - a
    return count
    

def main():
    """INT"""
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))


if __name__== "__main__":
    main()