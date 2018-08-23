def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    for i in range(len(m1)):
        for j in range(len(m2)):
            print([i + j for x, y in zip(first, second)])
            print([j + i for x, y in zip(first, second)])

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
    print(add_matrix(m1, m2))
    # multiply matrix 1 and matrix 2

if __name__ == '__main__':
    main()

# from numpy import * 

# x = int(input())

# y = reshape(x,(2,2)) 

# print(y)