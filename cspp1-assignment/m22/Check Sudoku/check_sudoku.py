'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    """sudoku"""
    for row in sudoku:
        for i in row:
            if i not in "123456789":
                return False
    i = 0
    for j in sudoku:
        if len(set(j)) == 9 and len(set(j[i])) == 9:
            return True
        return False
def main():
    """sudoku"""
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
