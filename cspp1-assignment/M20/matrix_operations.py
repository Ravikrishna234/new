"""MATRIXOPERATION"""
def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m1[0]) == len(m2):
        result=[[0 for i in range(len(m1))]for j in range(len(m1[0]))]
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                for k in range(len(m2)):
                    result[i][j] += int(m1[i][k]) * int(m2[k][j])
    return result
    else:
        print("Error: Matrix shapes Invalid for mult")
        return None

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        result =[[0 for j in range(len(m1))]for i in range(len(m1[0]))]
        result = [[int(m1[i][j]) + int(m2[i][j]) for j in range(len(m1))]for i in range(len(m1))]
    # for i in range(len(m1)):
    #     for j in range(len(m2)):
    #         result[i][j] += int(m1[i][j]) + int(m2[i][j])
        return result
    else:
        print("Error: Matrix shapes invalid for addition")
        return None

def read_matrix(l,l1):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    count = 0
    for i in range(len(l)):
        if len(l[i]) == len(l1[i]):
            count += 1
    if count == len(l):
        return True
    else:
        print("Error: Invalid input for the matrix")

def main():
    row1,col1 = map(int,input().split(','))
    l=[]
    l1=[]
    for i in range(1,row1+1):
        c=input().split()
        l.append(c)

    row2,col2 = map(int,input().split(','))
    for i in range(1,row2+1):
        c1=input().split()
        l1.append(c1)
    print(add_matrix(l,l1))
    print(mult_matrix(l,l1))
if __name__ == '__main__':
    main()

