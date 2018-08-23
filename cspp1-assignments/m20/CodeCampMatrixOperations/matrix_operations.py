import numpy as np
def mult_matrix(A, B):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    result = [[sum(a * b for a, b in zip(A_row, B_col))for B_col in zip(*B)]for A_row in A]
    print(result)
def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    # for i in m1:
    #     for j in m2:
    k = [i + j for x, y in zip(m1, m2) for i,j in zip(x, y)]
    if (len(m1[0]) == len(m2[0])):
        return [k[x:x+len(m1[1])] for x in range(0,len(k),len(m1[1]))]
    print('Error: Matrix shapes invalid for addition'                   )
    return None
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    n = input().split(',')
    rows = int(n[0])
    columns = int(n[1])
    matrix = []
    for row in range(rows):
        l = input().split(' ')
        if len(l) == rows:
            matrix.append([int(i) for i in l])
        else:
            print("Error: Invalid input for the matrix")
            return None
    return matrix

def main():
    # read matrix 1
    m1 = read_matrix()
    # add matrix 1 and matrix 2
    if m1 is None:
        exit()
    # read matrix 2
    m2 = read_matrix()
    if m2 is None:
        exit()
    print(add_matrix(m1, m2))
    print(mult_matrix(m1, m2))
    # multiply matrix 1 and matrix 2

if __name__ == '__main__':
    main()

# from numpy import * 

# x = int(input())

# y = reshape(x,(2,2)) 

# print(y)