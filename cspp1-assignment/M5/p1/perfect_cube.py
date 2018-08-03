"""guess and check perfect_cube.py"""
def main():
    """cube"""
    i = 0
    x_cu = int(input())
    for i in range(abs(x_cu)+1):
        if i**3 >= abs(x_cu):
            break
    if i ** 3 != abs(x_cu):
        print(x_cu, 'is not a perfect cube')
    else:
        if x_cu < 0:
            i = -i
    print('Cube root of ' + str(x_cu) + ' is ' + str(i))
if __name__ == "__main__":
    main()
