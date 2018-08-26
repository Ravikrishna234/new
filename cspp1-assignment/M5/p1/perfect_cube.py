"""guess and check perfect_cube.py"""
def main():
    """cube"""
    i = 0
    cube_ = int(input())
    for i in range(abs(cube_)+1):
        if i**3 >= abs(cube_):
            break
    if i ** 3 != abs(cube_):
        print(cube_, "is not a perfect cube")
    else:
        if cube_ < 0:
            i = -i
        print(cube_, "is a perfect cube")
if __name__ == "__main__":
    main()
