"""MATRIXOPERATION"""
def mult_matrix(m1_, m2_):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    result = [[0 for i in range(len(m1_))]for j in range(len(m2_[1]))]
    if len(m1_[0]) == len(m2_):
        for i in range(len(m1_)):
            for j in range(len(m2_[1])):
                for k in range(len(m2_)):
                    result[i][j] += int(m1_[i][k]) * int(m2_[k][j])
        return result
    print("Error: Matrix shapes invalid for mult")
    return None

def add_matrix(m1_, m2_):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    for i in range(len(m1_)):
        if len(m1_) == len(m2_) and len(m1_[i]) == len(m2_[i]):
            result = [[0 for j in range(len(m1_))]for i in range(len(m1_[0]))]
            result = [[int(m1_[i][j]) + int(m2_[i][j])for j in range(len(m1_[0]))]for i in range(len(m1_))]
    # for i in range(len(m1)):
    #     for j in range(len(m2)):
    #         result[i][j] += int(m1[i][j]) + int(m2[i][j])
            return result
    print("Error: Matrix shapes invalid for addition")
    return None
def read_matrix(matrix_1):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    for i in range(0, int(matrix_1[0])):
        column = input().split()
        if len(column) == int(matrix_1[1]):
            matrix.append(column)
        else:
            print("Error: Invalid input for the matrix")
            return None
    return matrix

def main():
    """Take Input"""
    # row1,col1 = map(int,input().split(','))
    # l=[]
    # l1=[]
    # for i in range(1,row1+1):
    #     c=input().split()
    #     l.append(c)
    # row2,col2 = map(int,input().split(','))
    # for i in range(1,row2+1):
    #     c1=input().split()
    #     l1.append(c1)
    # print(add_matrix(l,l1))
    # print(mult_matrix(l,l1))
    input_ = input()
    list1_ = input_.split(',')
    matrix_1 = read_matrix(list1_)
    input_ = input()
    list2_ = input_.split(',')
    matrix_2 = read_matrix(list2_)
    if matrix_1 is not None and matrix_2 is not None:
        print(add_matrix(matrix_1, matrix_2))
        print(mult_matrix(matrix_1, matrix_2))
if __name__ == '__main__':
    main()
