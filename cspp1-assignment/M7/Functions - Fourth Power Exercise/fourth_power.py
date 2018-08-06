"""fourth square"""
def square(x):
    """square"""
    x=x*x


def fourthPower(x):
    """square"""
    return x**4
   

def main():
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if(temp[1] == '0'):
        print(fourthPower(int(float(str(data)))))
    else:
        print(fourthPower(data))

if __name__== "__main__":
    main()
