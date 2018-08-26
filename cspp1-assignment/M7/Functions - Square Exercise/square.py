"""Function square"""
def square(x_square):
    """square"""
    x_square = x_square*x_square
    return x_square

def main():
    """square"""
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(square(int(float(str(data)))))
    else:
        print(square(data))

if __name__ == "__main__":
    main()
