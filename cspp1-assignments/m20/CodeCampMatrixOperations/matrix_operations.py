import numpy as np
def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    try:
        if len(m1) == len(m2[0]):
            pass
    except:
        return 'invalid matrix'

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    k = [i + j for x, y in zip(m1, m2) for i,j in zip(x, y)]
    return [k[x:x+len(m1)] for x in range(0,len(k),len(m1))]
def read_matrix(n):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    for row in range(int(n[0])):
        l = input().split(' ')
        matrix.append([int(l[i]) for i in range(len(l))])
    return matrix
def main():
    # read matrix 1
    m1 = read_matrix(input().split(','))
    # read matrix 2
    m2 = read_matrix(input().split(','))
    # add matrix 1 and matrix 2
    for i,j in m1,m2:
        if ' ' in (i or j):
            print('Error: Invalid input for the matrix')
            break
        elif len(i) != len(j):
            print('Error: Matrix shapes invalid for addition')
            break
        else:
            print(add_matrix(m1, m2))
    #print(mult_matrix(m1, m2))
    # multiply matrix 1 and matrix 2

if __name__ == '__main__':
    main()

# from numpy import * 

# x = int(input())

# y = reshape(x,(2,2)) 

# print(y)