'''
@author:navin106
matrix operations
'''
def mult_matrix(mat_1, mat_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(mat_1[1]) != len(mat_2):
        print("Error: Matrix shapes invalid for mult")
        return None
    else:
        result = [[sum(x * y for x, y in zip(m1_row, m2_col)) for m2_col in zip(*mat_2)] \
        for m1_row in mat_1]
        return result
def add_matrix(mat_1, mat_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(mat_1) == len(mat_2) and len(mat_1[0]) == len(mat_2[0]):
        k = [i + j for x, y in zip(mat_1, mat_2) for i, j in zip(x, y)]
        return [k[x:x+len(mat_1[1])] for x in range(0, len(k), len(mat_1[1]))]
    else:
        print("Error: Matrix shapes invalid for addition")
        return None
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    inp_list = input().split(',')
    rows = int(inp_list[0])
    #columns = int(inp_list[1])
    matrix = []
    for _ in range(int(rows)):
        temp_l = input().split(' ')
        if len(temp_l) == rows:
            matrix.append([int(i) for i in temp_l])
        else:
            matrix.append([int(i) for i in temp_l])
            print("Error: Invalid input for the matrix")
            return 0
    return matrix
def main():
    '''
    calling functions
    '''
    mat_1 = read_matrix()
    mat_2 = read_matrix()
    if mat_1 != 0 and mat_2 !=0:
        print(add_matrix(mat_1, mat_2))
        print(mult_matrix(mat_1, mat_2))
    else:
        pass
if __name__ == '__main__':
    main()
