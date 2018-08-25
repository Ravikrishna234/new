'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    """input"""
    lines_ = int(input())
    for _ in range(lines_):
        str_ = input()
        print(str_)

if __name__ == '__main__':
    main()
