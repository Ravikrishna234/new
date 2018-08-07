"""Recursion"""
def recurPower(base, exp):
    """recur"""
    if exp == 0:
        return 1:
    elif exp == 1:
        return base
    else:
        return base * recurPower(base,exp-1)

def main():
    """recur"""
    data = input()
    data = data.split()
    print(recurPower(float(data[0]),int(data[1])))   

if __name__ == "__main__":
    main()