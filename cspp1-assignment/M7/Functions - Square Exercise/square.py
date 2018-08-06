"""Function square"""
def square(x_sq):
    """square"""
    x_sq = x_sq*x_sq
    return x_sq

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
